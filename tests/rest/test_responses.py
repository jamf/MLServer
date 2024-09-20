from mlserver.types import InferenceRequest

from mlserver.rest.responses import ServerSentEvent


def test_sse_encode(inference_request: InferenceRequest):
    sse = ServerSentEvent(inference_request)
    encoded = sse.encode()
    as_string = encoded.decode("utf-8")

    expected_json = inference_request.model_dump_json().replace(" ", "")
    expected = f"data: {expected_json}\n\n"
    assert as_string == expected
