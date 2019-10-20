class PredictWeather (resource)

def get (self)
args=parser.parse_args()
district_query= arsg ['query']

dc_vectorized=model.dc_vectorizer_transform(
    np.array([district_query]))
    prediction= model.predict(dc_vectorized)
    pred_proba= model.predict_proba(dc_vectorized)

confidence=round(pred_proba[0],3)

if prediction==0
    text_pred='Negativo'
else:
    text_pred='Positivo'

output ={'prediction':text_pred,'confidence':confidence}

return output



