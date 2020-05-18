# +
import sklearn as skl
import numpy as np
import pandas as pd
import scipy.linalg as la
import scipy.stats as spstats


def base_forecast_linear(series, target_end_date = None, forecast_type="point", quantile=None):
    """
        Input:
        series: input time series of daily counts
        target_end_date: days forward to predict, default is two weeks hence
        forecast_type: point or quantile forecast
        quantile: quantile if quantile forecast
        
        Output:
        predict:  prediction using log linear model
    """
    series = series.copy()
    
    base_date = dt.datetime.strptime('01/01/20', '%m/%d/%y')
    end_date = series.index[-1] 
    if target_end_date is None:
        target_end_date = end_date+dt.timedelta(days=21) # default 3 week forecast
    
    if target_end_date < end_date:
        print('target_end_date before end of series, not valid forecast')
        raise ValueError
    
    
    # create prediction dates and dummy holder
    prediction_dates = pd.date_range(end_date + dt.timedelta(days=1), target_end_date)
    predictions = pd.Series(0, index=prediction_dates)
    predict_feats = featurize(predictions)
    
    # get input features and scale input and prediction features
    scaler = skl.preprocessing.StandardScaler()
    feats = featurize(series)
    feats_scaled = scaler.fit_transform(feats)
    predict_feats_scaled = scaler.transform(predict_feats)
    
    # fit linear model    
    lm = skl.linear_model.LinearRegression()
    target = series.map( lambda lnx : np.log(1+lnx), na_action='ignore')
    lm.fit( feats_scaled, target )
    
    # create point predictions
    log_predictions = pd.Series( lm.predict(predict_feats_scaled), index=prediction_dates )
    
    # compute stuff needed for quantiles
    noise_var = np.mean(  (lm.predict(feats_scaled) - target)**2)
    fish_mat_inv = feats_scaled.T.dot(feats_scaled) 
    beta_var, _, _,_ = la.lstsq( fish_mat_inv, predict_feats_scaled.T   )
    beta_var = predict_feats_scaled.dot(beta_var)
    predict_var  = np.diag(noise_var*beta_var)
    predict_std = np.sqrt(predict_var)
    # adjust for quantiles
    # using asymptotics now
    if forecast_type is "quantile": 
        log_predictions_quantile = log_predictions + predict_std*spstats.norm.ppf(quantile)
    else:
        quantile = 0.5 #not really necessary
        log_predictions_quantile = log_predictions
    
    
    # transform back
    predictions = log_predictions_quantile.map(lambda ilnx: np.exp(ilnx) - 1)
    
    return predictions
    


    
    
