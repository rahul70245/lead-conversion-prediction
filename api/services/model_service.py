from api.predictor import predict

def predict_source(data):
    return predict(model_type='Source',
                   data=data)


def predict_assigned(data):
    return predict(model_type='Assigned',
                   data = data)


def predict_dynamic(data):
    return predict(model_type='Dynamic',
                   data = data)