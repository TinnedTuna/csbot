import unittest
import csbot.plugins.log
import csbot.filefactories.inmemoryfilefactory
# Test the logging facilities.


class TestLogPlugin(unittest.TestCase):
    
    def setUp(self):
        self.f_factory=csbot.filefactories.inmemoryfilefactory.InMemoryFileFactory() 
        self.log_plugin = csbot.plugins.log.Log(self.f_factory);
    
    def testChannelHashToFile(self):
        self.assertEqual(self.log_plugin.channel_to_file('#cs-york'), 'cs-york.log')
        self.assertEqual(self.log_plugin.channel_to_file('##cs-york'), 'cs-york.log')
        self.assertEqual(self.log_plugin.channel_to_file('###cs-york'), 'cs-york.log')
        self.assertEqual(self.log_plugin.channel_to_file('cs-york'), 'cs-york.log')
        self.assertEqual(self.log_plugin.channel_to_file('c'), 'c.log')
        self.assertEqual(self.log_plugin.channel_to_file(''), '')


    def testJoin(self):
        self.log_plugin.join('Tinned_Tuna', '#cs-york')
        logfile = self.f_factory.get_files()[0]
        self.assertEqual(logfile.filename, 'cs-york.log') 


if __name__ == '__main__':
    unittest.main()
