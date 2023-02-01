import pytest
from src.lambda_function import PacientDetailService


class TestPacientDetailService:

    def test_givenLambdaFunctionCallThenReturnJsonResponse(self):
        _service = PacientDetailService()
        serviceResponse = _service.lambda_handler(any, any)
        assert serviceResponse['statusCode'] == 200
