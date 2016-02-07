require 'logger'

i = 0 # loop counter
num = 0	# process time counter
dir_path = "./files"
log = Logger.new('./getinfo.log', 'daily')
log.info("Program started")

while i < 1000 do
#	log.info("loop count : #{i}")
	filename = "#{[*1..9].sample(6).join}_log.txt"
	t_start = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
	file = File::stat("#{dir_path}#{filename}")
	log.info("#{filename} updated #{file.mtime.to_s}")
	t_end = Time.now.instance_eval { self.to_i * 1000 + (usec/1000) }
	t_pass = t_end - t_start
	num = num + t_pass
	i += 1
end
num = num / 1000.0 # get average ms
num = num / 1000.0 # ms to sec
log.info("Program end. average time : #{num} sec ")
