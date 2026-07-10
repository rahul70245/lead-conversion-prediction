# in this file we are defining schema of request and response


from pydantic import BaseModel, Field


class sourcerequest(BaseModel):
    lead_source : str


class assignedrequest(BaseModel):
    lead_source : str
    owner : str
    assigned_month : int
    assigned_year : int


class dynamicrequest(BaseModel):
    lead_source:int
    owner:str
    assigned_month:int = Field(ge=1,
                               le=12,
                               description="month should be between 1 and 12")
    assigned_year:int
    profile:str
    total_duration:float
    call_count:int
    distinct_call_days:int
    connected_call_count:int
    missed_call_count:int
    inbound_call_count:int
    outbound_call_count:int
    followup_done:int # need to check
    avaerage_duration:float
    connection_rate:float
    miss_rate:float
    average_call_per_day:float
    average_duration_per_day:float
    inbound_outbound_ratio:float
    time_taken_for_first_touch:float
    call_span_days:float
    call_frequency:float





class predictionresponse(BaseModel):
    prediction:int
    probability:float
    threshold:float


