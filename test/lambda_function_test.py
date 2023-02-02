from src.lambda_function import lambda_handler


class TestPacientDetailService:

    def test_givenLambdaFunctionCallThenReturnJsonResponse(self):
        serviceResponse = lambda_handler(any, any)
        assert serviceResponse['statusCode'] == 200
