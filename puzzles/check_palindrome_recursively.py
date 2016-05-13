class Palindrome(object):

	@staticmethod
	def is_palindrome(input_string):
		if len(input_string) in [0,1]:
			return True
		if input_string[0] == input_string[-1]:
			return Palindrome.is_palindrome(input_string[1:-2])
		return False
		
if __name__ == "__main__"
	print Palindrome.is_palindrome("")
	print Palindrome.is_palindrome("a")
	print Palindrome.is_palindrome("abcbcbasjfhiatjhuiweufh")
	print Palindrome.is_palindrome("abcdcba")