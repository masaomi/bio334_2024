sh make_multialigned_fa_from_snp_ref.sh
python calc_nd_fasta.py multialigned.fa
sh make_each_fa_from_snp_ref.sh
sh make_each_gene_fa_from_entire_fa.sh
grep '>' Ath_108_genes.fa |sed -e "s/>//" > gene_list.txt
python make_multialigned_each_gene_fa_batch.py gene_list.txt > make_multialigned_each_gene_fa_batch.sh
sh make_multialigned_each_gene_fa_batch.sh
python calc_genes_pi.py multialigned_gene_fastas > Athaliana_chr1_genes_pi.dat
python plot_pi.py
