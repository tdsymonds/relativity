relativity
===========
Coming soon...

Example usage:

.. code:: python

  from relativity.special import TimeDilation, LengthContradiction
  
  TimeDilation.get_proper_time(time=1, velocity=0.5)
  TimeDilation.get_proper_time(time=5, velocity=299792000, is_percent=False)
  TimeDilation.get_time_relative_ex_observer(time=1, velocity=0.5)

  LengthContradiction.get_proper_length(length=100, velocity=0.0447)
  LengthContradiction.get_proper_length(length=100, velocity=299792000, is_percent=False)
