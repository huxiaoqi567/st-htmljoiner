import sublime, sublime_plugin,re

class HtmlJoinerCommand(sublime_plugin.TextCommand):
	# str = '<div class="test"></div>'
	def run(self, edit):
		# self.view.insert(edit, 0, '<div class="test"></div>')
		 # print self.view.sel()
		selections = self.view.sel()
		# regions = self.view.find_all("\n");
		# print selections
		outstr = ""

		out_array = []
		# print selections
		for i in range(len(selections)):
			# print sublime.Region(regions[i].a,regions[i].b)
			# print self.view.substr(selections[i])
			outstr += self.view.substr(selections[i])

			# print outstr
			tmp_array = outstr.split("\n")
			# tmp_array = [1]
			for j in range(len(tmp_array)):
				# print tmp_array[i]['p']
				out_array.append(self.wrap(tmp_array[j]))

			# print "+\n".join(out_array)
			# print selections[i]
			# self.view.erase(edit,selections[i])
			self.view.replace(edit,selections[i],"+\n".join(out_array))

	def wrap(self,str):

		if re.match(r"\'",str):

			splitter = "\""

		else:

			splitter = "'"

		return splitter + str + splitter



        # if len(selections) == 1 and selections[0].empty():
        #     selections = [sublime.Region(0, self.view.size())]
		# print len(selections)
		# break
		# print re.match(r"\'",self.view)
