from django.urls import path, include
from .views import UserRegistrationViewSet, PrerecordedRecordingsViewSet, PrerecordedRecordingsImitationsViewSet, LiveRecordingsImitationsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('UserRegistration', UserRegistrationViewSet, basename='UserRegistration')
router.register('PrerecordedRecordings', PrerecordedRecordingsViewSet, basename='PrerecordedRecordings')
router.register('PrerecordedRecordingsImitations', PrerecordedRecordingsImitationsViewSet, basename='PrerecordedRecordingsImitations')
router.register('LiveRecordingsImitations', LiveRecordingsImitationsViewSet, basename='LiveRecordingsImitations')

urlpatterns = [
    path('', include(router.urls)),
]