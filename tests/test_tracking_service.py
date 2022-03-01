import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)

from tracking_service import TrackingService
def test_tracking_service():
    assert TrackingService

def test_tracking_service_get_from_tracking_more():
    # Arrange
    tracking_svc = TrackingService()
    tracking_number = '213ASD'

    # Act
    response = tracking_svc.get(tracking_number)

    # Assert
    assert response['tracking_number'] == tracking_number
    assert response['origin'] == 'TrackingMore'
