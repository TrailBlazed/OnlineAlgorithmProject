# Bitcoin Graph
<b>Aim :</b> Bitcoin address graph structural analysis


Two ways of creating Bitcoin address graph:
* get_block_data_latest(path,n_blocks): Generate address graph for transactions within 'n_blocks' number of latest blocks.
* get_block_data_early(path,b_hash,n_blocks) : Generate address graph for transactions within 'n_blocks' number of blocks starting from block having block hash as 'b_hash' .
<br>

<b>Graph Properties: </b>
* get_girvan_and_plot(G) : For detecting communities  in Bitcoin address graph(G)
* get_diameter(G): For calculating diameter of Bitcoin address graph(G)
* get_triangle_triadic(G) : For calculating triadic closure and triangle density of Bitcoin address graph(G)
* degree_distr(G) : For calculating degree distribution of Bitcoin address graph(G)