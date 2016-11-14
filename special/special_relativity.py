# -*- coding: utf-8 -*-
from __future__ import division

import math


class LorentzFactor(object):
    SPEED_OF_LIGHT = 299792458

    @staticmethod
    def get_beta(velocity, is_percent):
        if is_percent:
            return velocity
        return velocity / SPEED_OF_LIGHT

    @staticmethod
    def lorentz_factor(velocity, is_percent):
        beta = LorentzFactor.get_beta(velocity, is_percent)
        return 1 / (math.sqrt(1 - beta ** 2))


class TimeDilation(LorentzFactor):
    @staticmethod
    def get_proper_time(time, velocity, is_percent=True):
        return time * TimeDilation.lorentz_factor(velocity, is_percent)

    @staticmethod
    def get_time_relative_ex_observer(time, velocity, is_percent=True):
        """
        Dilation relative to an external observer
        """
        return time / TimeDilation.lorentz_factor(velocity, is_percent)
