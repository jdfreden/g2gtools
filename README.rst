===============================
g2gtools
===============================

.. image:: https://badge.fury.io/py/g2gtools.png
    :target: http://badge.fury.io/py/g2gtools

.. image:: https://travis-ci.org/churchill-lab/g2gtools.png?branch=master
    :target: https://travis-ci.org/churchill-lab/g2gtools

.. image:: https://anaconda.org/kbchoi/g2gtools/badges/version.svg
    :target: https://anaconda.org/kbchoi/g2gtools

.. image:: https://readthedocs.org/projects/g2gtools/badge/?version=latest
    :target: http://g2gtools.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/39776319.svg
    :target: https://zenodo.org/badge/latestdoi/39776319

**g2gtools** creates custom genomes by incorporating SNPs and indels into reference genome, extracts regions of interest, e.g., exons or transcripts, , and converts coordinates of files (bam, gtf, bed) between two genomes. Unlike other liftover tools, g2gtools does not throw away alignments that land on indel regions. Release Version 0.2 can now create personal **diploid** genomes. The new version still lifts over diploid alignments on personal genome coordinates back to that of reference so we can compare alignments from among samples in a population.

* Free software: MIT License
* Documentation for Release Ver. 0.2.XX: http://churchill-lab.github.io/g2gtools/.
* Documentation for Release Ver. 0.1.XX: https://g2gtools.readthedocs.org.


Reference
~~~~~~~~~

Manuscript in preparation (expected in 2018)

~~~~~~~~~
NOTE: Jake's Changes
~~~~~~~~~~
This fork was done to fix an issue I was having converting the coordinates of BAM file back to the reference system. I made a small change to the bsam.py 'convert_bam_file'. I did this because it was unclear what the original function required of the bam file and vci file headers. I have added comments explaining the issue in greater detail in the bsam.py file and will copy them here:

    I have made changes here because I did not understand what the original codes required from the vci_file and sam_file header.
    The original code seems to adjust the header appropriately by pushing the new header into 'tmp'
    but it then gives that contig the idx from the same file.
    This is a problem because vci_file.contigs returns a Dict which is unordered and will be different from the sam file header even if the contigs are in the same order in the vci file and the genome the reads were aligned to.

    
        Example.
            SAM FILE                VCI
            - chr1                  - chr1
            - chr2                  - chr2
            - chr3                  - chr3
              ...                     ...
              
            These files give the contigs in the same order in the header.
            In the sam_file object, the header is stored as in OrderedDict which keeps the order from the header.
            the vci_file stores the contigs in an ordinary dictionary which is unordered. Resulting in a case like this:
            
            SAM FILE                VCI
            - chr1                  - chr11
            - chr2                  - chrM
            - chr3                  - chr1
              ...                     ...
              
            In the original code, 'chr11' would get an idx of 11 because it would be the 11th contig in the sam file.
            However, later in the code when the alignments are being converted it refers the 11th idx in the VCI ordering
            which is estentially random due to it being an ordinary dict. 
