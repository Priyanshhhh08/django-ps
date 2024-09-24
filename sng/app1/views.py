from django.db import transaction
from django.shortcuts import render
from .models import TestModel
from .signal import my_signal

def emit_signal_in_transaction(request):
    try:
        with transaction.atomic():
            print("Inside transaction: Creating a new record in TestModel")
            TestModel.objects.create(name="Transaction Record")
            
            # Emit the signal inside the transaction
            my_signal.send(sender=None)
            
            # Simulate an error to force a rollback
            raise Exception("Forcing rollback")
    except Exception as e:
        print(f"Transaction failed: {e}")
    
    # Check if any records were created
    records = TestModel.objects.all()
    return render(request, 'index.html', {'records': records})
