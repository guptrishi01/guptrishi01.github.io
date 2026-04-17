"""
Portfolio project data.
Each project lives here as a dict. Editing this file is how you update
the site — no database, no admin panel needed.
"""

PROJECTS = [
    # ---------------- ACADEMIC PROJECTS ----------------
    {
        "slug": "sourdough-yeast-wgs",
        "category": "academic",
        "title": "Experimental Evolution of Sourdough Yeast",
        "subtitle": "Whole-Genome Sequencing Variant Analysis Pipeline",
        "date_range": "Jan 2025 – Sep 2025",
        "lab": "Heil Lab, NC State University",
        "role": "Undergraduate Research Assistant",
        "github": "https://github.com/guptrishi01/Sourdough_Yeast_WGS_Analysis",
        "tags": ["Bioinformatics", "Variant Calling", "Python", "R", "Bash", "GATK", "PCA", "Phylogenetics"],
        "hero_image": "img/projects/sourdough-hero.jpg",
        "summary": (
            "A full whole-genome sequencing pipeline built during my work in the Heil Lab, "
            "investigating how Saccharomyces cerevisiae populations adapt to the sourdough "
            "bread dough environment. The work spans raw FASTQ processing all the way to "
            "population-level variant analysis — SNVs, copy number variation, and loss of "
            "heterozygosity — and contributed to a peer-reviewed conference submission."
        ),
        "purpose": (
            "Yeast strains used in sourdough baking experience strong, consistent selective pressures — "
            "high sugar concentrations, acidity, and temperature fluctuation. The goal was to identify "
            "variants that arose specifically in response to the sourdough niche by comparing evolved "
            "populations to their ancestral strains and to nature-isolated counterparts."
        ),
        "methodology": [
            {
                "step": "Quality Control",
                "tools": "FastQC",
                "detail": "Generated per-sample QC reports (HTML + zip) on all paired-end reads via SLURM array jobs."
            },
            {
                "step": "Read Mapping",
                "tools": "BWA-MEM",
                "detail": "Mapped paired-end reads to the S. cerevisiae reference genome, producing per-sample SAM files."
            },
            {
                "step": "BAM Processing",
                "tools": "SAMtools, Picard",
                "detail": "SAM→BAM conversion, sort + index, MarkDuplicates for PCR duplicates, AddOrReplaceReadGroups, mapQ ≥ 20 filtering to remove unmapped/secondary/QC-fail reads."
            },
            {
                "step": "Per-Sample Variant Calling",
                "tools": "GATK HaplotypeCaller",
                "detail": "Called variants in GVCF mode (ERC GVCF) for each filtered BAM, producing one GVCF per sample."
            },
            {
                "step": "Consolidate GVCFs",
                "tools": "GATK GenomicsDBImport",
                "detail": "Consolidated all per-sample GVCFs into a shared GenomicsDB workspace per chromosome."
            },
            {
                "step": "Joint Genotyping",
                "tools": "GATK GenotypeGVCFs",
                "detail": "Jointly genotyped all samples per chromosome, leveraging cohort-wide information for higher-confidence calls."
            },
            {
                "step": "Merge VCFs",
                "tools": "Picard GatherVcfs",
                "detail": "Combined all 16 per-chromosome genotyped VCFs into one cohort-wide callset: all_chromosomes_combined.vcf."
            },
            {
                "step": "Hard Filtering",
                "tools": "GATK VariantFiltration",
                "detail": "Applied GATK best-practices filters: QD<2.0, FS>60.0, SOR>3.0, MQ<50.0, MQRankSum<-5.0, ReadPosRankSum<-4.0."
            },
            {
                "step": "Subsetting",
                "tools": "bcftools",
                "detail": "Split the callset into SD ancestor, NAT ancestor, SD descendants, NAT descendants; used bcftools isec to remove ancestral variants and retain only evolved ones."
            },
            {
                "step": "Annotation",
                "tools": "SnpEff + SnpSift",
                "detail": "Annotated functional effects (missense, synonymous, stop-gained, frameshift) and filtered to HIGH / MODERATE impact variants of interest."
            },
            {
                "step": "Downstream Analysis",
                "tools": "Python (Jupyter), R (SNPRelate)",
                "detail": "Built LOH heatmaps, CNV gain/loss tables across 16 chromosomes, PCA plots, and neighbor-joining phylogenetic trees."
            },
        ],
        "code_snippet": {
            "language": "bash",
            "caption": "GATK joint genotyping shell script (simplified)",
            "code": """#!/bin/bash
#SBATCH --job-name=joint_geno
#SBATCH --array=1-16
#SBATCH --mem=32G
#SBATCH --time=12:00:00

# Map the SLURM array ID to a chromosome
CHROM=$(sed -n "${SLURM_ARRAY_TASK_ID}p" chromosomes.txt)

gatk --java-options "-Xmx28g" GenotypeGVCFs \\
    -R newref.fasta \\
    -V gendb://${CHROM}_gdb \\
    -O ${CHROM}_genotyped_variants.vcf

echo "Finished joint genotyping for ${CHROM}"
"""
        },
        "results": [
            "Identified 26,207 high-coverage and 33,867 low-coverage copy number variation sites across all 16 chromosomes.",
            "Produced genome-wide LOH heatmaps revealing distinct signatures in sourdough vs. nature-isolated populations.",
            "PCA and neighbor-joining phylogeny cleanly separated sourdough, nature, and commercial yeast isolates.",
            "Contributed figures and analyses to Demystifying Domestication of Sourdough Yeast: Evolution, Diversity, and Metabolism — submitted to the International Conference on Yeast Genetics and Molecular Biology.",
        ],
        "skills_gained": [
            "GATK best-practices variant calling pipeline from FASTQ to annotated VCF",
            "Orchestrating large compute jobs on a SLURM-managed HPC cluster",
            "Variant annotation and functional impact filtering (SnpEff / SnpSift)",
            "Population genomics: PCA, phylogenetics (SNPRelate in R), IBS distance matrices",
            "CNV and LOH detection with custom Python windowing analyses",
            "Reproducible pipeline engineering — each step scripted, versioned, and documented",
        ],
        "what_i_learned": (
            "This was my first real introduction to production-scale bioinformatics. I learned the difference "
            "between running a tool once and building a pipeline that survives hundreds of samples — error "
            "handling, resuming from partial runs, checkpointing, and designing scripts that are reusable. "
            "More importantly, I learned how the biology constrains the computation: why GVCF-then-joint-"
            "genotype works better than calling variants sample-by-sample, why CNV analysis needs per-sample "
            "normalization, and how to read a phylogeny critically rather than trusting any single tool's "
            "output."
        ),
    },
    {
        "slug": "surgeonfish-cnn",
        "category": "academic",
        "title": "Surgeonfish Species Detection",
        "subtitle": "CNN-Based Morphological Analysis and Phylogenetic Inference",
        "date_range": "Aug 2025 – Present",
        "lab": "Dornburg Lab, UNC Charlotte",
        "role": "Graduate Research Assistant",
        "github": "https://github.com/guptrishi01/Surgeonfish_Neural_Network_Phylogenetics",
        "tags": ["Machine Learning", "Computer Vision", "PyTorch", "YOLOv8", "Python", "SLURM", "HPC"],
        "hero_image": "img/projects/surgeonfish-hero.jpg",
        "summary": (
            "An ongoing graduate research project training a YOLOv8 convolutional neural network to "
            "automatically detect and classify six species of surgeonfish from underwater images. The "
            "goal is to investigate whether CNN-extracted morphological features carry phylogenetic "
            "signal — that is, whether pattern-based classification recovers evolutionary relationships."
        ),
        "purpose": (
            "Manual identification of fish species from images is slow, subjective, and error-prone. "
            "Automating the task with a CNN frees researchers to analyze larger image sets and — more "
            "interestingly — lets us quantify morphological features that are hard to measure by hand. "
            "If those learned features correlate with phylogeny, that's a novel tool for morphometric "
            "evolutionary biology."
        ),
        "methodology": [
            {
                "step": "Image Preprocessing",
                "tools": "Python, OpenCV, Pillow",
                "detail": "Standardized 83 raw underwater images — corrected for illumination differences, orientation variance, and background noise; applied data augmentation (flips, color jitter, random crops) to expand the effective training set."
            },
            {
                "step": "Dataset Preparation",
                "tools": "Custom Python scripts, YOLOv8 format",
                "detail": "Converted annotations to YOLOv8 format (normalized bounding boxes, per-class txt files), split into train/val/test with stratified sampling across all 6 species."
            },
            {
                "step": "Model Training",
                "tools": "PyTorch, Ultralytics YOLOv8",
                "detail": "Fine-tuned YOLOv8 pretrained weights (COCO) on the surgeonfish dataset. Configured training hyperparameters: batch size, learning rate schedule, image size, augmentation intensity."
            },
            {
                "step": "HPC Training",
                "tools": "SLURM, GPU partitions",
                "detail": "Submitted training jobs to UNCC's HPC cluster, requesting GPU partitions (A100s) for parallel hyperparameter sweeps. Cut training iteration time vs. local CPU-only runs."
            },
            {
                "step": "Evaluation",
                "tools": "Python, scikit-learn, matplotlib",
                "detail": "Computed precision, recall, mAP (mean average precision) at IoU 0.5 and 0.5:0.95, per-class confusion matrices, and error analysis to identify which species pairs the model confuses most."
            },
            {
                "step": "Phylogenetic Comparison (ongoing)",
                "tools": "Python, R",
                "detail": "Extracting feature embeddings from the trained CNN and comparing clustering against the known surgeonfish phylogeny."
            },
        ],
        "code_snippet": {
            "language": "python",
            "caption": "YOLOv8 training launch script (excerpt)",
            "code": """from ultralytics import YOLO

# Fine-tune YOLOv8 on surgeonfish detection
model = YOLO("yolov8m.pt")  # medium variant, pretrained on COCO

results = model.train(
    data="surgeonfish.yaml",       # dataset config
    epochs=150,
    imgsz=640,
    batch=16,
    device=0,                      # CUDA GPU 0
    optimizer="AdamW",
    lr0=1e-3,
    cos_lr=True,                   # cosine LR schedule
    augment=True,                  # mosaic + color jitter
    patience=20,                   # early stop
    project="runs/surgeonfish",
    name="yolov8m_run1",
)

# Validate on held-out test set
metrics = model.val(data="surgeonfish.yaml", split="test")
print(f"mAP@0.5: {metrics.box.map50:.3f}")
print(f"mAP@0.5:0.95: {metrics.box.map:.3f}")
"""
        },
        "results": [
            "Successfully training a YOLOv8 detector across 6 surgeonfish species from 83 preprocessed images (project ongoing — metrics updated as training sweeps complete).",
            "Preprocessing pipeline reduced per-image variance in lighting and orientation, improving early-epoch convergence.",
            "HPC-enabled hyperparameter sweeps completed in roughly the time a single local run would take.",
            "Ongoing: extracting model embeddings to test for phylogenetic signal.",
        ],
        "skills_gained": [
            "End-to-end computer vision workflow: data curation, annotation, training, validation",
            "PyTorch and the Ultralytics YOLO ecosystem",
            "Hyperparameter tuning on an HPC cluster using SLURM",
            "Quantitative evaluation of detection models (precision, recall, mAP, confusion matrices)",
            "Applying deep learning to biological research questions",
        ],
        "what_i_learned": (
            "Transfer learning is a lever — starting from COCO pretrained weights instead of scratch "
            "is the difference between a workable model on 83 images and never converging. I also "
            "learned how much of CV research is data work, not model work: once preprocessing was solid, "
            "architectural tweaks mattered far less than I expected. And working on HPC forced me to "
            "think carefully about reproducibility — every run is a checkpoint, every config file is "
            "versioned, or you lose track of what worked."
        ),
    },
    {
        "slug": "translation-msa-tool",
        "category": "academic",
        "title": "Translation-Based Multiple Sequence Alignment Tool",
        "subtitle": "Codon-Aware Pairwise Alignment via Protein-Level Needleman-Wunsch",
        "date_range": "Sep 2025 – Dec 2025",
        "lab": "UNC Charlotte — Programming II Final Project",
        "role": "Individual Project",
        "github": "https://github.com/guptrishi01/Translation-Based_Multiple_Sequence_Alignment_Tool",
        "tags": ["Python", "Biopython", "Algorithms", "Bioinformatics", "pytest", "CLI"],
        "hero_image": "img/projects/msa-hero.jpg",
        "summary": (
            "A Python command-line MSA pipeline that aligns nucleotide sequences by translating them to "
            "amino acids, pairwise aligning at the protein level with Needleman-Wunsch, and back-"
            "translating to codon-aware DNA alignments. Built from scratch for my Programming II "
            "final project — no external alignment libraries used."
        ),
        "purpose": (
            "Direct nucleotide alignment ignores the fact that coding sequences evolve under selective "
            "pressure at the protein level. Aligning amino acids first respects that biology: "
            "synonymous substitutions don't disrupt alignment, and frame-shift indels are impossible "
            "by construction. This project was an exercise in reimplementing a classical algorithm "
            "from first principles while respecting biological reality."
        ),
        "methodology": [
            {
                "step": "ORF Detection",
                "tools": "Custom Python",
                "detail": "Scans all six reading frames for open reading frames using configurable translation tables (standard, mitochondrial, etc.)."
            },
            {
                "step": "Translation",
                "tools": "Biopython, custom codon tables",
                "detail": "Translates nucleotide sequences to amino acids using the chosen translation table."
            },
            {
                "step": "K-mer Sorting",
                "tools": "Custom Python",
                "detail": "Computes pairwise k-mer similarity scores between all protein sequences, then orders them to drive progressive alignment from the most similar pair outward."
            },
            {
                "step": "Pairwise Alignment",
                "tools": "Custom Needleman-Wunsch",
                "detail": "Implements the Needleman-Wunsch dynamic programming algorithm with configurable match / mismatch / indel scores. Produces amino acid alignments with gap characters."
            },
            {
                "step": "Back-Translation",
                "tools": "Custom Python",
                "detail": "Maps the aligned amino acids back to their original codons, preserving reading frame — a gap in the protein alignment becomes three dashes in the DNA alignment."
            },
            {
                "step": "Variability Analysis",
                "tools": "pandas, matplotlib",
                "detail": "Computes per-codon-position mismatch and indel rates, exports CSV summaries, and plots mutation rates across the alignment to visualize conserved vs. variable regions."
            },
            {
                "step": "Testing",
                "tools": "pytest",
                "detail": "Unit tests cover ORF detection (known-ORF inputs, edge cases like sequences with no ORF), k-mer ordering (symmetry, correct pair identification), and alignment correctness (known-alignment fixtures)."
            },
        ],
        "code_snippet": {
            "language": "python",
            "caption": "Needleman-Wunsch core (excerpt)",
            "code": """def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, indel=-2):
    \"\"\"Global alignment of two amino acid sequences via dynamic programming.\"\"\"
    n, m = len(seq1), len(seq2)
    # Initialize scoring matrix
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = i * indel
    for j in range(1, m + 1):
        dp[0][j] = j * indel

    # Fill matrix
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = match if seq1[i-1] == seq2[j-1] else mismatch
            dp[i][j] = max(
                dp[i-1][j-1] + score,     # diagonal (match/mismatch)
                dp[i-1][j] + indel,       # up (gap in seq2)
                dp[i][j-1] + indel,       # left (gap in seq1)
            )

    # Traceback to recover alignment
    aligned1, aligned2 = [], []
    i, j = n, m
    while i > 0 and j > 0:
        score = match if seq1[i-1] == seq2[j-1] else mismatch
        if dp[i][j] == dp[i-1][j-1] + score:
            aligned1.append(seq1[i-1]); aligned2.append(seq2[j-1]); i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j] + indel:
            aligned1.append(seq1[i-1]); aligned2.append("-"); i -= 1
        else:
            aligned1.append("-"); aligned2.append(seq2[j-1]); j -= 1
    while i > 0: aligned1.append(seq1[i-1]); aligned2.append("-"); i -= 1
    while j > 0: aligned1.append("-"); aligned2.append(seq2[j-1]); j -= 1

    return "".join(reversed(aligned1)), "".join(reversed(aligned2)), dp[n][m]
"""
        },
        "results": [
            "Produced codon-aware DNA alignments from raw FASTA nucleotide input with full traceability through amino acid space.",
            "Generated CSV summaries of codon-position variability and matplotlib plots of per-position mismatch / indel rates.",
            "Full pytest test suite covering ORF detection, k-mer ordering, and alignment correctness passes on CI.",
            "CLI supports configurable match/mismatch/indel scoring, translation tables, k-mer size, and reference sequence for mutation-rate analysis.",
        ],
        "skills_gained": [
            "Dynamic programming algorithms (Needleman-Wunsch from first principles)",
            "Codon-aware biological sequence manipulation with Biopython",
            "Designing and testing a reusable Python CLI (argparse + modular package structure)",
            "Unit testing with pytest including fixtures, parametrization, and edge-case coverage",
            "Data visualization with matplotlib for variability analysis",
        ],
        "what_i_learned": (
            "Writing Needleman-Wunsch yourself teaches you far more than calling a library wrapper. The "
            "traceback step especially — recovering the alignment from the scoring matrix — is deceptively "
            "subtle. I also learned that the 'translation-first' design isn't just an academic exercise; "
            "it genuinely produces better alignments on coding sequences because it respects the reading "
            "frame. The project pushed me to think of bioinformatics tools as software products: modular, "
            "tested, documented, reusable."
        ),
    },

    # ---------------- PERSONAL PROJECTS ----------------
    {
        "slug": "court-iq",
        "category": "personal",
        "title": "Court IQ — AI Tennis Coach",
        "subtitle": "Generative AI-Powered Tennis Match Analysis",
        "date_range": "Oct 2025 – Present",
        "lab": "Personal Project",
        "role": "Sole Developer",
        "github": "https://github.com/guptrishi01/court-iq",
        "tags": ["FastAPI", "Python", "SQL", "Generative AI", "LLM", "REST API", "Prompt Engineering"],
        "hero_image": "img/projects/court-iq-hero.jpg",
        "summary": (
            "A personal tool that uses generative AI to help me improve at tennis. I record my matches "
            "on my phone, review the footage, log point-by-point data, and write down what went well and "
            "what didn't. An LLM then analyzes everything together to deliver specific coaching — "
            "strategies to try, drills to practice, conditioning to work on, and patterns I'd never spot "
            "on my own."
        ),
        "purpose": (
            "Good tennis coaches are expensive and rare. What most players actually need isn't a human "
            "coach — it's someone objective looking at their data and saying 'your first-serve "
            "percentage collapses in third sets, conserve energy on second-serve points in the first "
            "two.' LLMs are great at that kind of pattern-matching once you feed them structured data. "
            "The hard part is the structured data — so that's what I built first."
        ),
        "methodology": [
            {
                "step": "Database Schema Design",
                "tools": "SQL (normalized relational model)",
                "detail": "Three normalized tables — Match, Set, Point — where every aggregate statistic (first-serve %, break-point conversion, winner/UE ratio, hold %) is derived by querying Point-level data. No redundant storage; one source of truth."
            },
            {
                "step": "Backend API",
                "tools": "FastAPI, Pydantic, SQLAlchemy",
                "detail": "Full CRUD for matches, including nested creation with sets and points in a single request. List, get, delete endpoints. Input validation via Pydantic models."
            },
            {
                "step": "Stats Engine",
                "tools": "Python, SQL queries",
                "detail": "A derived-stats endpoint that computes every tennis statistic on demand from Point-level data. Adding a new stat is a one-function change — no migrations, no schema tweaks."
            },
            {
                "step": "AI Coaching — Single Match",
                "tools": "LLM API, prompt engineering",
                "detail": "Pipes a match's stats plus the player's own pros/cons self-reflection into a carefully structured prompt. The LLM returns tactical adjustments, drills, and physical conditioning recommendations."
            },
            {
                "step": "AI Coaching — Multi-Match Trends",
                "tools": "LLM API, context assembly",
                "detail": "Aggregates the last N matches into a trend-analysis prompt. Spots patterns that only show up across matches — e.g., break-point conversion drops on hot days, or backhand unforced errors spike when returning second serves."
            },
            {
                "step": "Workflow (player-side)",
                "tools": "iPhone, web form",
                "detail": "Mount phone on court fence, record match, review footage afterward, log point-by-point through the web interface, write 3 pros / 3 cons, request coaching. Full loop."
            },
        ],
        "code_snippet": {
            "language": "python",
            "caption": "FastAPI derived-stats endpoint (excerpt)",
            "code": """from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/matches", tags=["matches"])


@router.get("/{match_id}/stats")
def get_match_stats(match_id: int, db: Session = Depends(get_db)):
    \"\"\"Compute all derived statistics for a match from raw point data.\"\"\"
    match = db.query(Match).filter(Match.id == match_id).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")

    points = (
        db.query(Point)
          .join(Set).filter(Set.match_id == match_id)
          .all()
    )

    # First serve %
    first_serves = [p for p in points if p.server_is_me]
    first_serve_pct = (
        sum(1 for p in first_serves if p.first_serve_in) / len(first_serves)
        if first_serves else 0
    )

    # Winner / unforced error ratio
    winners = sum(1 for p in points if p.outcome == "winner")
    ues     = sum(1 for p in points if p.outcome == "unforced_error")
    w_ue_ratio = round(winners / ues, 2) if ues else None

    # Break-point conversion (points where I was returning and opponent was at 0/15/30 x 40)
    bp_opps    = [p for p in points if p.is_break_point_for_me]
    bp_convert = (
        sum(1 for p in bp_opps if p.point_winner == "me") / len(bp_opps)
        if bp_opps else 0
    )

    return {
        "match_id": match_id,
        "first_serve_pct": round(first_serve_pct, 3),
        "winner_ue_ratio": w_ue_ratio,
        "break_point_conversion": round(bp_convert, 3),
        "total_points": len(points),
    }
"""
        },
        "results": [
            "Normalized 3-table schema (Match / Set / Point) with every aggregate derived from raw point data — no storage redundancy.",
            "FastAPI backend implements full CRUD plus derived stats and two AI coaching endpoints.",
            "Single-match LLM insight generation produces tactical, drill, and conditioning recommendations grounded in the match data plus the player's own reflections.",
            "Multi-match trend analysis identifies patterns across match history (e.g., serve-percentage drops by set number, break-point conversion trends).",
            "Next milestones: frontend UI for match logging, performance dashboard with charts, deployment.",
        ],
        "skills_gained": [
            "Relational schema design with normalization (3NF) and derived-stat philosophy",
            "FastAPI + Pydantic + SQLAlchemy for production Python APIs",
            "Nested request validation and CRUD API design",
            "Prompt engineering for domain-specific LLM outputs (sports coaching)",
            "Context assembly — turning raw structured data into LLM-ready prompts",
            "Personal product thinking: identifying a real need, designing the data first, then layering AI on top",
        ],
        "what_i_learned": (
            "The data schema is 80% of the work on an AI app. Once your structured data is clean, the "
            "LLM part is almost trivial — prompt engineering matters, but it's a layer, not a foundation. "
            "I also learned the real value of 'derive everything, store nothing': when I wanted to add a "
            "new stat (first-serve-return-win %), I wrote one Python function and it just worked, no "
            "migrations. That's been the biggest payoff of the normalized design."
        ),
    },
]


def get_project(slug):
    for p in PROJECTS:
        if p["slug"] == slug:
            return p
    return None


def get_projects_by_category(category):
    return [p for p in PROJECTS if p["category"] == category]
