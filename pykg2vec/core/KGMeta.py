#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Abstract class for the Knowledge graph models"""
from abc import ABCMeta

class ModelMeta:
	__metaclass__ = ABCMeta

	def __init__(self):
		"""Initializing and create the model to be trained and inferred"""
		pass

	def train(self):
		"""function to train the model"""
		pass

	def test(self):
		"""function to test the model"""
		pass

	def embed(self,h, r, t):
		"""function to get the embedding value"""
		pass

class TrainerMeta:
	__metaclass__ = ABCMeta

	def __init__(self):
		"""Initializing and create the model to be trained and inferred"""
		pass

	def build_model(self):
		pass

	def train_model(self):
		pass

	def save_model(self, sess):
		"""function to save the model"""
		pass

	def load_model(self, sess):
		"""function to load the model"""
		pass

class VisualizationMeta:
	__metaclass__ = ABCMeta
	
	def __init__(self):
		"""Initializing and create the model to be trained and inferred"""
		pass
		
	def display(self):
		"""function to display embedding"""
		pass

	def summary(self):
		"""function to print the summary"""
		pass

class EvaluationMeta:
	__metaclass__ = ABCMeta

	def __init__(self):
		pass

	def relation_prediction(self):
		pass

	def entity_classification(self):
		pass

	def relation_classification(self):
		pass

	def triple_classification(self):
		pass

	def entity_completion(self):
		pass
