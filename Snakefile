rule reproduce_all:
    input:
        "results/top_50_staff.csv",
        "results/PCE_map.html",
        "results/ipeds_pce_scatter.html"

rule prepare_data:
    input:
        "data/Table.xlsx",
        "data/AcademicLibrary.csv"
    output:
        "data/state_code.csv",
        "data/interim_data/PCE_clean.csv",
        "data/interim_data/IPED_clean.csv",
        "data/interim_data/IPED_by_State.csv"
    shell:
        "python scripts/data_prepare.py"

rule data_analysis:
    input:
        "data/interim_data/IPED_clean.csv"
    output:
        "results/top_50_staff.csv",
        "results/top_50_salary.csv",
        "results/number_of_staff_ranked_by_state.csv",
        "results/salary_by_state_ranked.csv"
    shell:
        "python scripts/data_analysis.py"

rule pce_integration:
    input:
        "data/interim_data/PCE_clean.csv",
        "data/state_code.csv"
    output:
        "data/interim_data/PCE_total.csv"
        "data/interim_data/PCE_sub.csv"
    shell:
        "python scripts/PCE_integration.py"

rule ipeds_integration:
    input:
        "data/interim_data/IPED_by_State.csv",
        "data/interim_data/PCE_total.csv"
    output:
        "data/interim_data/IPED_PCE.csv"
    shell:
        "python scripts/IPEDs_integration.py"

rule map_plot:
    input:
        "data/interim_data/PCE_total.csv",
        "data/interim_data/PCE_sub.csv"
    output:
        "results/PCE_map.html"
    shell:
        "python scripts/PCE_map.py"

rule scatter_plot:
    input:
        "data/interim_data/IPED_PCE.csv"
    output:
        "results/ipeds_pce_scatter.html"
    shell:
        "python scripts/ipeds_pce_scatter.py"

