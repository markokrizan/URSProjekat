Za testiranje potrebno je kreirati posebno virtualno okruzenje
virtualenv NAZIV_OKRUZENJA

Aktivirati okruzenje sa komandom
Linux 

source NAZIV_OKRUZENJA/bin/activate

Windows

NAZIV_OKRUZENJA\Scripts\activate

u virtualnom okruzenju instalirati py.test koristeci pip

pip install pytest

pre pokretanja testova potrebno je dodati putanju do src foldera u PYTHONPATH
Linux
export PYTHONPATH=$PYTHONPATH:putanja_do_src_foldera

Windows
set PYTHONPATH=%PYTHONPATH%;putanja_do_src_foldera

testovi se pokrecu tako sto se predje u folder gde su napisani moduli za testiranje i pokrene se komanda

py.test