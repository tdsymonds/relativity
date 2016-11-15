relativity
===========
Coming soon...

Example usage:

.. code:: python

  from relativity.special import special_relativity
  from relativity.general import general_relativity
  
  special_relativity.TimeDilation.get_proper_time(time=1, velocity=0.5)
  special_relativity.TimeDilation.get_proper_time(time=5, velocity=299792000, is_percent=False)
  special_relativity.TimeDilation.get_time_relative_ex_observer(time=1, velocity=0.5)

  special_relativity.LengthContradiction.get_proper_length(length=100, velocity=0.0447)
  special_relativity.LengthContradiction.get_proper_length(length=100, velocity=299792000, is_percent=False)
