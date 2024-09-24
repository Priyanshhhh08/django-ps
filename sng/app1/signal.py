from django.db import models
from django.dispatch import Signal, receiver

# Define a custom signal
my_signal = Signal()

# Signal handler that performs a database operation
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    from .models import TestModel  # Import the model here to avoid circular import
    print("Signal handler: Creating a new record in TestModel")
    TestModel.objects.create(name="Signal Record")
