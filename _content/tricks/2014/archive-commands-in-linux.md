# Archive Commands in Linux

- date: 2014-01-07 19:13
- tags: linux, shell
- category: tricks

----------------------------

Below is a collection of commands compressing and uncompressing various file formats.  

```bash

#### compress ####
$ tar -cvf output.tar test-files
$ gzip output.tar 		# result file "output.tar.gz"
$ tar -cvzf output.tar.gz test-files		# combined with the two above
$ bzip2 output.tar		# result file "output.tar.bz2"
$ tar -cvjf output.tar.bz2 test-files
# other formats (zip, gz, rar, 7z, ...)
$ zip -r archive.zip test-files
$ star -cv f=output.star test-files
$ find test-dir | cpio -ov > output.cpio
$ 7z a archive.7z test-files	# the package name for 7z is "p7zip"

####  list files in the archive ####
$ tar -tvf file.tar
$ star -tv f=file.tar
$ unzip -l file.zip
$ cpio -t < file.cpio
$ 7z l file.7z

#### uncompress ####
# tar
$ tar xvf file.tar
$ tar xvzf file.tar.gz
$ tar xvzf file.tar.tgz
$ tar xvjf file.tar.bz2
$ tar xvjf file.tar.tbz2
# other formats 
$ gunzip file.**gz**	
$ bunzip2 file.**bz2**
$ uncompress file.**Z**
$ unzip file.zip
$ unrar x file.rar		# or "$ rar x file.rar"
$ 7z x file.**7z		# or "$ 7z e file.7z**"
$ star -xv f=archive.star 
$ cpio -idmv < archive.cpio
$ unace x file.ace
 

```
 
