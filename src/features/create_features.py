class Features(object):
	'''Extract image features from lines of image text.
	Use a config file to extract numcep and numcontext.''' 
	def __init__(self, config):
		self.config = config
