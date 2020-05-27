# +
import datetime as dt
import pandas as pd
import sklearn.linear_model as skllin
import sklearn.kernel_ridge as sklker
import numpy as np
import scipy.linalg as la
import scipy.stats as spstats
import features
import sklearn

# def rolling_forecast(series,
#                      forecast_func=base_forecast_linear,
#                      target_end_date=None, 
#                      forecast_type="point", 
#                      quantile=None, 
#                      stride=7, 
#                      width=28):
#     """
#         Creates a rolling forecast out of base forecast 
#     """
    



def base_forecast_linear(series, 
                         target_date_range = None, 
                         forecast_type="point", 
                         quantile=None, 
                        weights=None):
    """
        Input:
        series: input time series of daily counts
        target_date_range: range of dates predict, default is start to three weeks hence
        forecast_type: point or quantile forecast
        quantile: quantile if quantile forecast
        weights: weighing for samples, allows to create rolling forecasts
        
        Output:
        predict:  prediction using log linear model
    """
    series = series.copy()
    
    base_date = dt.datetime.strptime('01/01/20', '%m/%d/%y')
    end_date = series.index[-1]
    start_date = series.index[0]
    if target_date_range is None: # default three weeks ahead forecast
        target_end_date = end_date + dt.timedelta(days=21)
        target_date_range = pd.date_range(start_date, target_end_date) 
    
#     if target_end_date < end_date:
#         print('target_end_date before end of series, not valid forecast')
#         raise ValueError
    
    
    # create prediction dates and dummy holder
    prediction_dates = target_date_range.copy()
    predictions = pd.Series(0, index=prediction_dates)
    predict_feats = features.featurize(predictions)
    
    
    # get input features and scale input and prediction features
    scaler = sklearn.preprocessing.StandardScaler(with_mean=False)
    feats = features.featurize(series)
    # standardize all features 
    feats_scaled = scaler.fit_transform(feats)
    predict_feats_scaled = scaler.transform(predict_feats)
    
    # create target
    target = series.map( lambda lnx : np.log(1+lnx), na_action='ignore')

    
    # fit linear model  
    # remove intercept because its included explicitly in features above
    lm = skllin.LinearRegression(fit_intercept=False) 
    # weight the samples if necessary
    weighted_feats_scaled = feats_scaled.copy()
    weighted_target = target.copy()
    if weights is not None:
        weighted_feats_scaled = np.diag(weights**0.5).dot(feats_scaled)
        weighted_target = (weights**0.5) * target
    
    lm.fit( weighted_feats_scaled, weighted_target )
    
    # create point predictions
    log_predictions = pd.Series( lm.predict(predict_feats_scaled), index=prediction_dates )
    
    # compute stuff needed for quantiles
    noise_var = np.mean(  (lm.predict(weighted_feats_scaled) - weighted_target)**2)
    fish_mat_inv = weighted_feats_scaled.T.dot(weighted_feats_scaled) 
    beta_var, _, _,_ = la.lstsq( fish_mat_inv, predict_feats_scaled.T   )
    beta_var = predict_feats_scaled.dot(beta_var)
    predict_var  = np.diag(noise_var*beta_var)
    predict_std = np.sqrt(predict_var)
    
    # adjust for quantiles
    # using asymptotics now
    if quantile is None: # quantile is none so make it 0.5 or null
        quantile = 0.5 
    log_predictions_quantile = log_predictions + predict_std*spstats.norm.ppf(quantile)

    # transform back
    predictions = log_predictions_quantile.map(lambda ilnx: np.exp(ilnx) - 1)
    
    return predictions
    


    
    
