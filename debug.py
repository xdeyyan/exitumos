from exitum import os *
from exitum import debugger *
from exitum import gui
from exitum import window

class debug(**properties)
	 print("Loading properties...")
	 hide_label(self.err_msg.text) 
def debugger
	self.header.text = 'Welcome to Exitum Debugger!'
	self.debug_area.input = 'Debug Log'
	newLine.add
	codeInput.input = self.input
	if self.input contains:
	 unknown.command = self.err_msg.text = 'Command not found'
	else:
	 print('Command exectuded' + codeInput.input)
pass

def commands
	if input:
		'exitum update'
		run.Download('http://download.exitum.ga/exitum-os/exitum_os.zip')
		'exitum downgrade'
		run.Download('http://download.exitum.ga/exitum-os/downgrade-previous/exitum_os_old.zip')
		'get app ' + exitum.SourceApp
		run.Download('http://download.exitum.ga/apps/ ' + exitum.SourceApp)
		run.Install(exitum.SourceApp)
		run.InstallDialog(exitum.SourceApp)
		'exitum info'
		if input 'exitum update' exec:
		info.Download('http://properties.exitum.ga/prop.exi')
		print(exitum.Version)
		print(exitum.ID)
		print(exitum.INFOS)
pass