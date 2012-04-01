import sublime
import sublime_plugin
import os

class RooterCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.find_root()

	def find_root(self):
		self.view = self.window.active_view()
		self.cur_dir = os.path.dirname(self.view.file_name())
		os.chdir(self.cur_dir)	
		sublime.status_message("Set root directory %15s" %(self.cur_dir))
	
		
