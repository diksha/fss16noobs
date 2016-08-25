import utest
from utest import ok
from utest import oks
@ok
def _newTest():
  "This test fails"
  assert 1==0, "equality failure"

oks()