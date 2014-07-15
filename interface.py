import extraction
import ginger
import ranking


def phase1(filename):
    extraction.check()
    ginger.main(filename)
    extraction.classify("corrected.txt")
    extraction.mine("comments.txt")
    return

def phase2():
    ranking.rank('explicit.txt','implicit.txt')
    return

if __name__=="__main__":
    print "--: Wellcome to Feature Extractor :--\n"
    phase1("sample.txt")
    phase2()
