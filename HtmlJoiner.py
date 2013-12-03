import sublime, sublime_plugin,re

class HtmlJoinerCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		selections = self.view.sel()

		outstr = ""

		out_array = []

		for i in range(len(selections)):

			outstr += self.view.substr(selections[i])

			tmp_array = outstr.split("\n")

			for j in range(len(tmp_array)):

				out_array.append(self.__join(tmp_array[j]))

			self.view.replace(edit,selections[i],"+\n".join(out_array))

	def __toggle(self,str):

		if re.search(r"^('|\"|\+)|('|\"|\+)$",str):
			print "unjoin"
			return self.__unjoin(self,str)

		else:
			print "join"
			return self.__join(self,str)

	def __join(self,str):
		
		if re.search("\'",str):

			splitter = "\""

		else:

			splitter = "'"

		return splitter + str + splitter

	def __unjoin(self,str):

		return re.sub(r"^('|\"|\+)|('|\"|\+)$","",str)




