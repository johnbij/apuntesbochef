# ── DIM ──────────────────────────────────────────────────────
from clases.dim.dm01 import render_DM01
from clases.dim.dm02 import render_DM02
from clases.dim.dm03 import render_DM03
from clases.dim.dm04 import render_DM04
from clases.dim.dm05 import render_DM05

# ── DFI ──────────────────────────────────────────────────────
from clases.dfi.df01 import render_DF01
from clases.dfi.df02 import render_DF02
from clases.dfi.df03 import render_DF03
from clases.dfi.df04 import render_DF04
from clases.dfi.df05 import render_DF05

# ── DII ──────────────────────────────────────────────────────
from clases.dii.di01 import render_DI01
from clases.dii.di02 import render_DI02
from clases.dii.di03 import render_DI03
from clases.dii.di04 import render_DI04
from clases.dii.di05 import render_DI05

# ── DCC ──────────────────────────────────────────────────────
from clases.dcc.dc01 import render_DC01
from clases.dcc.dc02 import render_DC02
from clases.dcc.dc03 import render_DC03
from clases.dcc.dc04 import render_DC04
from clases.dcc.dc05 import render_DC05

from utils import render_proximamente

CONTENIDOS = {
    "🔢 DIM": {
        "color_subcats": "rojo",
        "subcategorias": {
            "Cálculo": {
                "DM01": {"label": "📖 DM01: Próximamente", "render": render_DM01},
                "DM02": {"label": "📖 DM02: Próximamente", "render": render_DM02},
                "DM03": {"label": "📖 DM03: Próximamente", "render": render_DM03},
            },
            "Álgebra Lineal": {
                "DM04": {"label": "📖 DM04: Próximamente", "render": render_DM04},
                "DM05": {"label": "📖 DM05: Próximamente", "render": render_DM05},
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
                "DF01": {"label": "📖 DF01: Próximamente", "render": render_DF01},
                "DF02": {"label": "📖 DF02: Próximamente", "render": render_DF02},
                "DF03": {"label": "📖 DF03: Próximamente", "render": render_DF03},
            },
            "Electromagnetismo": {
                "DF04": {"label": "📖 DF04: Próximamente", "render": render_DF04},
                "DF05": {"label": "📖 DF05: Próximamente", "render": render_DF05},
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
                "DI01": {"label": "📖 DI01: Próximamente", "render": render_DI01},
                "DI02": {"label": "📖 DI02: Próximamente", "render": render_DI02},
                "DI03": {"label": "📖 DI03: Próximamente", "render": render_DI03},
            },
            "Estadística": {
                "DI04": {"label": "📖 DI04: Próximamente", "render": render_DI04},
                "DI05": {"label": "📖 DI05: Próximamente", "render": render_DI05},
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
                "DC01": {"label": "📖 DC01: Próximamente", "render": render_DC01},
                "DC02": {"label": "📖 DC02: Próximamente", "render": render_DC02},
                "DC03": {"label": "📖 DC03: Próximamente", "render": render_DC03},
            },
            "Programación": {
                "DC04": {"label": "📖 DC04: Próximamente", "render": render_DC04},
                "DC05": {"label": "📖 DC05: Próximamente", "render": render_DC05},
            },
            "Ejercitación": {
                "DCE01": {"label": "📝 DCE01: Próximamente", "render": lambda: render_proximamente("DCE01")},
                "DCE02": {"label": "📝 DCE02: Próximamente", "render": lambda: render_proximamente("DCE02")},
            },
        },
    },
}
