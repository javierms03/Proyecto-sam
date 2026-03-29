#!/usr/bin/env nextflow


params.sam = 'WT.sam'


process analyze_sam {
    input:
    path sam_file

    output:
    stdout

    script:
    """
    uv run ${projectDir}/main.py ${sam_file}
    """
}

workflow {
    analyze_sam(file(params.sam)) | view
}
