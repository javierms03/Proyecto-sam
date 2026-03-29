#!/usr/bin/env nextflow

// 1. Recibe --sam como parámetro
params.sam = 'WT.sam'

// 2. Ejecuta un proceso analyze_sam
process analyze_sam {
    input:
    path sam_file

    output:
    stdout

    script:
    // 3. Llama a tu script Python con uv indicando la ruta completa al script
    """
    uv run ${projectDir}/main.py ${sam_file}
    """
}

workflow {
    analyze_sam(file(params.sam)) | view
}
