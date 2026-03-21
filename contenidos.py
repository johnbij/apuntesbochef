# ── DIM · Cálculo ────────────────────────────────────────────
from clases.dim.calculo.c01 import render_C01
from clases.dim.calculo.c02 import render_C02
from clases.dim.calculo.c03 import render_C03

# ── DIM · Álgebra Lineal ────────────────────────────────────
from clases.dim.algebra_lineal.al01 import render_AL01
from clases.dim.algebra_lineal.al02 import render_AL02

# ── DFI · Mecánica ──────────────────────────────────────────
from clases.dfi.mecanica.m01 import render_M01
from clases.dfi.mecanica.m02 import render_M02
from clases.dfi.mecanica.m03 import render_M03

# ── DFI · Electromagnetismo ─────────────────────────────────
from clases.dfi.electromagnetismo.em01 import render_EM01
from clases.dfi.electromagnetismo.em02 import render_EM02

# ── DII · Optimización ──────────────────────────────────────
from clases.dii.optimizacion.op01 import render_OP01
from clases.dii.optimizacion.op02 import render_OP02
from clases.dii.optimizacion.op03 import render_OP03

# ── DII · Estadística ───────────────────────────────────────
from clases.dii.estadistica.est01 import render_EST01
from clases.dii.estadistica.est02 import render_EST02

# ── DCC · Algoritmos ────────────────────────────────────────
from clases.dcc.algoritmos.ag01 import render_AG01
from clases.dcc.algoritmos.ag02 import render_AG02
from clases.dcc.algoritmos.ag03 import render_AG03

# ── DCC · Programación ──────────────────────────────────────
from clases.dcc.programacion.pg01 import render_PG01
from clases.dcc.programacion.pg02 import render_PG02

from utils import render_proximamente

CONTENIDOS = {
    "🔢 DIM": {
        "color_subcats": "rojo",
        "subcategorias": {
            "Cálculo": {
                "C01": {"label": "📖 C01: Próximamente", "render": render_C01},
                "C02": {"label": "📖 C02: Próximamente", "render": render_C02},
                "C03": {"label": "📖 C03: Próximamente", "render": render_C03},
            },
            "Álgebra Lineal": {
                "AL01": {"label": "📖 AL01: Próximamente", "render": render_AL01},
                "AL02": {"label": "📖 AL02: Próximamente", "render": render_AL02},
            },
            "Ejercitación": {
                "DME01": {"label": "📝 DME01: Próximamente", "render": lambda: render_proximamente("DME01")},
                "DME02": {"label": "📝 DME02: Próximamente", "render": lambda: render_proximamente("DME02")},
            },
        },
    },
    "📉 DFI": {
        "color_subcats": "verde",
        "subcategorias": {
            "Mecánica": {
                "M01": {"label": "📖 M01: Próximamente", "render": render_M01},
                "M02": {"label": "📖 M02: Próximamente", "render": render_M02},
                "M03": {"label": "📖 M03: Próximamente", "render": render_M03},
            },
            "Electromagnetismo": {
                "EM01": {"label": "📖 EM01: Próximamente", "render": render_EM01},
                "EM02": {"label": "📖 EM02: Próximamente", "render": render_EM02},
            },
            "Ejercitación": {
                "DFE01": {"label": "📝 DFE01: Próximamente", "render": lambda: render_proximamente("DFE01")},
                "DFE02": {"label": "📝 DFE02: Próximamente", "render": lambda: render_proximamente("DFE02")},
            },
        },
    },
    "📐 DII": {
        "color_subcats": "morado",
        "subcategorias": {
            "Optimización": {
                "OP01": {"label": "📖 OP01: Próximamente", "render": render_OP01},
                "OP02": {"label": "📖 OP02: Próximamente", "render": render_OP02},
                "OP03": {"label": "📖 OP03: Próximamente", "render": render_OP03},
            },
            "Estadística": {
                "EST01": {"label": "📖 EST01: Próximamente", "render": render_EST01},
                "EST02": {"label": "📖 EST02: Próximamente", "render": render_EST02},
            },
            "Ejercitación": {
                "DIE01": {"label": "📝 DIE01: Próximamente", "render": lambda: render_proximamente("DIE01")},
                "DIE02": {"label": "📝 DIE02: Próximamente", "render": lambda: render_proximamente("DIE02")},
            },
        },
    },
    "📊 DCC": {
        "color_subcats": "naranja",
        "subcategorias": {
            "Algoritmos": {
                "AG01": {"label": "📖 AG01: Próximamente", "render": render_AG01},
                "AG02": {"label": "📖 AG02: Próximamente", "render": render_AG02},
                "AG03": {"label": "📖 AG03: Próximamente", "render": render_AG03},
            },
            "Programación": {
                "PG01": {"label": "📖 PG01: Próximamente", "render": render_PG01},
                "PG02": {"label": "📖 PG02: Próximamente", "render": render_PG02},
            },
            "Ejercitación": {
                "DCE01": {"label": "📝 DCE01: Próximamente", "render": lambda: render_proximamente("DCE01")},
                "DCE02": {"label": "📝 DCE02: Próximamente", "render": lambda: render_proximamente("DCE02")},
            },
        },
    },
}
