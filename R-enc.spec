#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-enc
Version  : 0.2.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/enc_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/enc_0.2.0.tar.gz
Summary  : Portable Tools for 'UTF-8' Character Data
Group    : Development/Tools
License  : GPL-3.0
Requires: R-enc-lib
Requires: R-readr
BuildRequires : R-readr
BuildRequires : clr-R-helpers

%description
Implements an S3 class for storing 'UTF-8' strings, based on regular character vectors.
    Also contains routines to portably read and write 'UTF-8' encoded text files,
    to convert all strings in an object to 'UTF-8',
    and to create character vectors with various encodings.

%package lib
Summary: lib components for the R-enc package.
Group: Libraries

%description lib
lib components for the R-enc package.


%prep
%setup -q -c -n enc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532311197

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1532311197
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library enc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library enc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library enc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library enc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/enc/DESCRIPTION
/usr/lib64/R/library/enc/INDEX
/usr/lib64/R/library/enc/Meta/Rd.rds
/usr/lib64/R/library/enc/Meta/features.rds
/usr/lib64/R/library/enc/Meta/hsearch.rds
/usr/lib64/R/library/enc/Meta/links.rds
/usr/lib64/R/library/enc/Meta/nsInfo.rds
/usr/lib64/R/library/enc/Meta/package.rds
/usr/lib64/R/library/enc/NAMESPACE
/usr/lib64/R/library/enc/NEWS.md
/usr/lib64/R/library/enc/R/enc
/usr/lib64/R/library/enc/R/enc.rdb
/usr/lib64/R/library/enc/R/enc.rdx
/usr/lib64/R/library/enc/help/AnIndex
/usr/lib64/R/library/enc/help/aliases.rds
/usr/lib64/R/library/enc/help/enc.rdb
/usr/lib64/R/library/enc/help/enc.rdx
/usr/lib64/R/library/enc/help/paths.rds
/usr/lib64/R/library/enc/html/00Index.html
/usr/lib64/R/library/enc/html/R.css
/usr/lib64/R/library/enc/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/enc/libs/enc.so
/usr/lib64/R/library/enc/libs/enc.so.avx2
/usr/lib64/R/library/enc/libs/enc.so.avx512
