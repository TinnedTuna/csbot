from csbot.core import Plugin, PluginFeatures
import csbot.filefactories.standardfilefactory.StandardFileFactory


class EmptyPlugin(Plugin):
    pass


class Log(Plugin):
    features = PluginFeatures()

    def __init__(self, file_factory=None):
        if (file_factory==None):
            self.file_factory= csbot.filefactories.standardfilefactory.StandardFileFactory('base_dir')
        else:
            self.file_factory = file_factory
        # A dictionary of channels to files
        channel_files = {}
        
    def channel_to_file(self, channel=None):
        # First, strip off any leading '#' chars, as is common on freenode.
        if (channel is None or len(channel) == 0):
            return ''
        while (channel[0] == '#'):
            channel = channel[1:]
        return channel+'.log'

    def get_channel_file(self, channel):
        # If there is a channel file associated with this channel, get it
        # Else open a new one and store it.
        if (channel_files.has_key(channel)):
             current_channel_file = channel_files[channel]
        else:
             current_channel_file = file_factory.open_file(channel_to_file(channel), 'w')
             channel_files[channel] = current_channel_file
        return current_channel_file
    

    @features.hook('join')
    def join(self, user, channel):
        # Get the current channel file:
        current_channel_file = self.get_channel_file(channel)
        current_channel_file.write("{0} --> {1]\n".format(self.time(),user))
        current_channel_file.flush()
 
    @features.hook('part')
    def part(self,user,channel):
        # Get the current channel file:
        current_channel_file = self.get_channel_file(channel)
        current_channel_file.write("{0} <-- {1}\n".format(self.time(), user))
        current_channel_file.flush()

    @features.hook('privmsg')
    def privmsg(self, user, channel, msg):
        # Get the current channel file:
        current_channel_file = self.get_channel_file(channel)
        current_channel_file.write("{0} {1}: {2}\n".format(self.time(),user,msg))
        current_channel_file.flush()

    @features.hook('action')
    def action(self, user, channel, action):
        # Get the current channel file:
        current_channel_file = self.get_channel_file(channel)
        # Write the action with a timestamp.
        current_channel_file.write("{0} * {1} {2}\n".format(self.time(),user,action))
        current_channel_file.flush()
