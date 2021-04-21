from g2gtools import bsam

# bsam.convert_bam_file(vci_file="../../CC_RIX_Liver_2021/snakemake_pipe/CC_Genomes/CC025/CC025.vci.gz",
#                       file_in="../../CC_RIX_Liver_2021/snakemake_pipe/g2gtools_investigation/small_MOM.bam",
#                       file_out="../../CC_RIX_Liver_2021/snakemake_pipe/g2gtools_investigation/g2gtools_invest_1.bam",
#                       reverse=True)

bsam.convert_bam_file(vci_file="../../CC_RIX_Liver_2021/snakemake_pipe/CC_Genomes/CC011/CC011.vci.gz",
                      file_in="../../CC_RIX_Liver_2021/snakemake_pipe/g2gtools_investigation/small_DAD.bam",
                      file_out="../../CC_RIX_Liver_2021/snakemake_pipe/g2gtools_investigation/g2gtools_invest_2.bam",
                      reverse=True)
