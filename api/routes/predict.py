from fastapi import APIRouter

from api.schemas import (sourcerequest,assignedrequest,
                     dynamicrequest,predictionresponse)


from api.services.model_service import(predict_source,
                                   predict_assigned,
                                   predict_dynamic)



router = APIRouter(prefix="/predict",
                   tags=['Lead Conversion Prediction'])


@router.post("/source",response_model=predictionresponse)

def source_prediction(request:sourcerequest):
    result = predict_source(request.model_dump())
    return result




@router.post("/assigned",response_model=predictionresponse)

def assigned_prediction(request:assignedrequest):
    result = predict_assigned(request.model_dump())
    
    return result



@router.post("/dynamic",response_model=predictionresponse)

def dynamic_prediction(request:dynamicrequest):
    result=predict_dynamic(request.model_dump())

    return result


