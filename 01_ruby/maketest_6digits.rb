require 'fileutils'
require 'logger'
require 'benchmark'

i = 0 # loop counter
num = 0	# file name counter
log = Logger.new('./filemake.log', 'daily') # make log file at current directory
log.info("Program started")

dir_path = "./files"
FileUtils.mkdir_p(dir_path) unless FileTest.exist?(dir_path)

result = Benchmark.realtime do
	while i < 1000000 do
		num = "%06d" % i
		FileUtils.touch("#{dir_path}/#{num}.txt")
		i += 1
	end
end
log.info("Program end : #{result} sec passed")
