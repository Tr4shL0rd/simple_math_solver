alphabet = [chr(i) for i in range(65,65+25)]
def main(startLine:int | None=None, endLine:int | None=None):
	if startLine <= 0:
		startLine = 0
	if endLine <= 0:
		endLine = 100000
	with open("notes.txt", "r") as f:
		lines = f.readlines()
		for i,line in enumerate(lines):
			if not line.startswith("#"):	
				if i < startLine:
					pass
				else:
					exec(f"print(alphabet[i],':',{line.rsplit('=')[0]})")
				if i > endLine:
					break
if __name__ == "__main__":
	startLine = 5
	endLine = -1
	main(startLine, endLine)