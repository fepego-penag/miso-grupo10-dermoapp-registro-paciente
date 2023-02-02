from src.lambda_function import *


class TestPacientDetailService:

    def test_givenLambdaFunctionCallThenReturnJsonResponse(self):
        serviceResponse = lambda_handler(any, any)
        assert serviceResponse['statusCode'] == 200

    def test_givenLambdaFunctionCallThenReturnJsonResponse2(self):
        serviceResponse = lambda_handler_duplication(any, any)
        assert serviceResponse['statusCode'] == 200

    def test_givenLambdaFunctionCallThenReturnJsonResponse2(self):
        serviceResponse = lambda_handler_duplication2(any, any)
        assert serviceResponse['statusCode'] == 200