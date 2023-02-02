from src.lambda_function import *


class TestPacientDetailService:

    def test_givenLambdaFunctionCallThenReturnJsonResponse(self):
        serviceResponse = lambda_handler(any, any)
        assert serviceResponse['statusCode'] == 200