import sublime
import sublime_plugin

class RooterCommand(sublime_plugin.TextCommand):
	"""docstring for Rooter"""
	def run(self, edit):
		sublime.status_message("Set root directory")
		
