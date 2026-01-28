from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "roles.json")


def load_roles():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def home():
    return jsonify({"message": "ECE Roadmap API is running ✅"})


@app.route("/api/roles", methods=["GET"])
def get_roles():
    roles = load_roles()

    search = request.args.get("search", "").lower().strip()
    domain = request.args.get("domain", "").lower().strip()

    if search:
        roles = [r for r in roles if search in r["title"].lower()]

    if domain and domain != "all":
        roles = [r for r in roles if r["domain"].lower() == domain]

    return jsonify(roles)


@app.route("/api/roles/<role_id>", methods=["GET"])
def get_role(role_id):
    roles = load_roles()
    role = next((r for r in roles if r["id"] == role_id), None)

    if not role:
        return jsonify({"error": "Role not found"}), 404

    return jsonify(role)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

# import os
# import json
# from flask import Flask, jsonify, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # -----------------------------
# # PATHS
# # -----------------------------
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_DIR = os.path.join(BASE_DIR, "data")
# DATA_PATH = os.path.join(DATA_DIR, "roles.json")


# # -----------------------------
# # DEFAULT 25 ROLES DATA
# # -----------------------------
# DEFAULT_ROLES = [
#     {
#         "id": "rtl-design",
#         "title": "RTL Design Engineer",
#         "domain": "VLSI",
#         "shortDescription": "Design digital logic using Verilog/SystemVerilog, create micro-architecture and write synthesizable RTL.",
#         "tools": ["Verilog", "SystemVerilog", "Vivado", "Synopsys Design Compiler", "Questa/ModelSim", "Git"],
#         "fundamentals": [
#             "Digital Electronics (Combinational + Sequential)",
#             "FSM Design",
#             "Timing Concepts (setup/hold)",
#             "Pipelining",
#             "Clocking & Reset Strategies",
#             "Bus protocols basics (AXI/APB)",
#         ],
#         "roadmap": {
#             "basic": [
#                 "Learn Verilog syntax and write small modules (adder, mux, counter)",
#                 "Understand FSMs and write FSM-based controllers",
#                 "Practice testbenches (basic)",
#                 "Understand synthesizable vs non-synthesizable RTL",
#                 "Use Git and basic Linux commands"
#             ],
#             "intermediate": [
#                 "Write SystemVerilog RTL + interfaces",
#                 "Design pipelined datapaths (ALU, MAC, FIFO)",
#                 "Handle CDC basics and resets properly",
#                 "Understand constraints basics (SDC)",
#                 "Work with synthesis reports (area, timing, power)"
#             ],
#             "expert": [
#                 "Architect complex blocks (DMA, cache, interconnect)",
#                 "Low-power design concepts (clock gating, power gating basics)",
#                 "Design for test readiness (scan-friendly RTL)",
#                 "Performance optimization and timing closure aware RTL",
#                 "Work with SOC-level integration & debug"
#             ]
#         },
#         "projects": [
#             "UART controller",
#             "FIFO + Arbiter",
#             "Simple RISC-V single-cycle CPU",
#             "AXI-lite peripheral"
#         ],
#         "opportunities": [
#             "Semiconductor companies (Intel, AMD, Qualcomm, Nvidia)",
#             "VLSI service companies",
#             "Startups in chip design"
#         ]
#     },

#     {
#         "id": "physical-design",
#         "title": "Physical Design Engineer",
#         "domain": "VLSI",
#         "shortDescription": "Convert synthesized netlist into layout: floorplan, placement, CTS, routing and signoff.",
#         "tools": ["Cadence Innovus", "Synopsys ICC2", "PrimeTime", "Linux", "TCL"],
#         "fundamentals": [
#             "CMOS basics",
#             "Standard cells and libraries",
#             "P&R flow",
#             "Timing closure",
#             "IR drop & EM basics",
#             "DRC/LVS concepts"
#         ],
#         "roadmap": {
#             "basic": [
#                 "Learn ASIC flow overview (RTL → GDSII)",
#                 "Understand floorplanning basics",
#                 "Learn placement & routing concepts",
#                 "Basics of timing (setup/hold) and slack",
#                 "TCL scripting fundamentals"
#             ],
#             "intermediate": [
#                 "CTS concepts and skew optimization",
#                 "Fix congestion and DRC issues",
#                 "ECO flows",
#                 "Basics of power planning",
#                 "PrimeTime report reading"
#             ],
#             "expert": [
#                 "Advanced timing closure strategies",
#                 "Signoff: IR/EM, SI, Crosstalk",
#                 "Multi-corner multi-mode (MCMM)",
#                 "Physical verification signoff",
#                 "Flow automation and productivity scripting"
#             ]
#         },
#         "projects": [
#             "Small block PnR in open-source tools (OpenROAD)",
#             "Timing closure case study",
#             "CTS optimization experiment"
#         ],
#         "opportunities": ["ASIC design houses", "EDA companies", "Foundry ecosystem"]
#     },

#     {
#         "id": "design-verification",
#         "title": "Design Verification Engineer (UVM)",
#         "domain": "VLSI",
#         "shortDescription": "Verify RTL correctness using SystemVerilog/UVM, testbenches, assertions and coverage.",
#         "tools": ["SystemVerilog", "UVM", "Questa", "VCS", "Verdi", "Python"],
#         "fundamentals": [
#             "Digital design concepts",
#             "OOP concepts (important for UVM)",
#             "Testbench architecture",
#             "Functional coverage",
#             "Assertions (SVA)",
#             "Debugging skills"
#         ],
#         "roadmap": {
#             "basic": [
#                 "Learn SystemVerilog basics + testbench writing",
#                 "Understand clocking, reset, transactions",
#                 "Write directed tests for simple RTL",
#                 "Learn basic assertions",
#                 "Learn coverage basics"
#             ],
#             "intermediate": [
#                 "Build UVM environment (driver, monitor, scoreboard)",
#                 "Constrained random testing",
#                 "Functional + code coverage closure",
#                 "Debug using waveform + logs",
#                 "Regression setup"
#             ],
#             "expert": [
#                 "System-level verification strategy",
#                 "Formal verification basics",
#                 "Reusable VIP creation",
#                 "Performance regression automation",
#                 "Debug complex corner-case bugs"
#             ]
#         },
#         "projects": ["UVM verification of FIFO", "UVM for UART", "AXI-lite UVM environment"],
#         "opportunities": ["Chip companies", "EDA companies", "Verification services"]
#     },

#     {
#         "id": "dft-engineer",
#         "title": "DFT Engineer (Design For Test)",
#         "domain": "VLSI",
#         "shortDescription": "Insert scan chains, ATPG patterns and ensure manufacturability/testing of chips.",
#         "tools": ["Synopsys DFT Compiler", "TetraMAX", "Cadence Modus", "TCL"],
#         "fundamentals": [
#             "Scan chains",
#             "ATPG basics",
#             "Fault models (stuck-at, transition)",
#             "JTAG basics",
#             "Test coverage concepts",
#             "DFT architecture"
#         ],
#         "roadmap": {
#             "basic": [
#                 "Understand why DFT is needed",
#                 "Learn scan chain concept",
#                 "Learn stuck-at faults",
#                 "Basic DFT insertion flow overview"
#             ],
#             "intermediate": [
#                 "ATPG pattern generation",
#                 "Coverage improvement techniques",
#                 "Boundary scan (JTAG) basics",
#                 "DFT constraints and reporting"
#             ],
#             "expert": [
#                 "Advanced DFT (MBIST/LBIST)",
#                 "Diagnosis flows",
#                 "Yield improvement analysis",
#                 "Complex SOC-level DFT integration"
#             ]
#         },
#         "projects": ["Scan insertion mini-flow", "ATPG pattern study"],
#         "opportunities": ["Manufacturing test teams", "SOC DFT teams"]
#     },

#     {
#         "id": "analog-layout",
#         "title": "Analog Layout Engineer",
#         "domain": "VLSI",
#         "shortDescription": "Create analog/mixed-signal layout with matching, symmetry, and parasitic-aware design.",
#         "tools": ["Cadence Virtuoso", "Assura/Calibre", "Spectre", "PEX tools"],
#         "fundamentals": [
#             "Analog circuit basics",
#             "Device matching",
#             "Layout techniques (common centroid, interdigitation)",
#             "Parasitics (R/C)",
#             "DRC/LVS",
#             "Latch-up & guard rings"
#         ],
#         "roadmap": {
#             "basic": [
#                 "Understand MOS devices and analog blocks",
#                 "Learn DRC/LVS workflow",
#                 "Basic layout of inverter, current mirror",
#                 "Understand matching and symmetry"
#             ],
#             "intermediate": [
#                 "Layout op-amp, bandgap, LDO blocks",
#                 "Parasitic extraction awareness",
#                 "Noise, shielding, guard rings",
#                 "EM/IR basics for analog"
#             ],
#             "expert": [
#                 "High-speed layout practices",
#                 "RF layout basics",
#                 "Analog signoff and silicon debug support",
#                 "Process variation aware layout"
#             ]
#         },
#         "projects": ["Layout current mirror", "Layout OTA", "Layout LDO"],
#         "opportunities": ["Analog/RF design teams", "Mixed-signal IC companies"]
#     },

#     {
#         "id": "sta-engineer",
#         "title": "STA Engineer (Static Timing Analysis)",
#         "domain": "VLSI",
#         "shortDescription": "Analyze and close timing across corners and modes using timing constraints and reports.",
#         "tools": ["Synopsys PrimeTime", "Tempus", "TCL", "SDC"],
#         "fundamentals": [
#             "Setup/hold timing",
#             "Clock definitions",
#             "Constraints (SDC)",
#             "Timing paths and slack",
#             "MCMM concepts",
#             "Crosstalk basics"
#         ],
#         "roadmap": {
#             "basic": [
#                 "Understand setup/hold and slack",
#                 "Learn SDC basics (create_clock, set_input_delay)",
#                 "Read timing reports",
#                 "Identify critical paths"
#             ],
#             "intermediate": [
#                 "MCMM timing analysis",
#                 "False paths and multicycle paths",
#                 "Fix timing with ECO guidance",
#                 "Clock tree understanding"
#             ],
#             "expert": [
#                 "Signoff timing closure",
#                 "Crosstalk and SI timing",
#                 "Advanced constraints debugging",
#                 "Timing methodology ownership"
#             ]
#         },
#         "projects": ["STA report analysis", "SDC constraints practice"],
#         "opportunities": ["Signoff teams", "Physical design signoff"]
#     },

#     # -------------- EXTRA ROLES (Total 25) --------------
#     {
#         "id": "fpga-design",
#         "title": "FPGA Design Engineer",
#         "domain": "Embedded + VLSI",
#         "shortDescription": "Develop digital systems on FPGA using HDL, IP cores and hardware debugging.",
#         "tools": ["Xilinx Vivado", "Intel Quartus", "Verilog", "SystemVerilog", "ILA", "Logic Analyzer"],
#         "fundamentals": ["HDL", "Timing constraints", "Clock domains", "Interfaces (UART/SPI/I2C)"],
#         "roadmap": {
#             "basic": ["Learn Verilog", "Blink LED, counters, PWM", "UART basic TX/RX"],
#             "intermediate": ["AXI basics", "DDR basics", "Timing closure in FPGA", "ILA debugging"],
#             "expert": ["High-speed design", "PCIe/Ethernet IP", "SoC FPGA integration", "Performance optimization"]
#         },
#         "projects": ["UART on FPGA", "SPI sensor interface", "Mini RISC CPU on FPGA"],
#         "opportunities": ["Defense", "Telecom", "Automotive", "Hardware startups"]
#     },

#     {
#         "id": "communication-engineer",
#         "title": "Communication Engineer",
#         "domain": "Communication",
#         "shortDescription": "Work on wireless/wired communication systems: modulation, coding, RF concepts and networks.",
#         "tools": ["MATLAB", "Simulink", "GNU Radio", "Python", "NS-3"],
#         "fundamentals": ["Signals & Systems", "Probability", "Digital Communication", "Information theory basics"],
#         "roadmap": {
#             "basic": ["Learn modulation (ASK/FSK/PSK/QAM)", "Learn sampling & FFT", "Basics of antennas"],
#             "intermediate": ["OFDM", "Channel coding", "MIMO basics", "5G NR basics"],
#             "expert": ["Link-level simulation", "RF impairments modeling", "Protocol stack understanding", "Research + optimization"]
#         },
#         "projects": ["OFDM simulation", "QAM BER simulation", "Simple SDR receiver"],
#         "opportunities": ["Telecom companies", "5G R&D", "Networking firms"]
#     },

#     {
#         "id": "embedded-engineer",
#         "title": "Embedded Systems Engineer",
#         "domain": "Embedded",
#         "shortDescription": "Develop firmware for microcontrollers and embedded products using C/C++ and RTOS.",
#         "tools": ["C", "C++", "STM32", "Arduino", "FreeRTOS", "Keil", "VS Code"],
#         "fundamentals": ["C programming", "Microcontroller basics", "Interrupts", "UART/SPI/I2C", "Timers"],
#         "roadmap": {
#             "basic": ["Learn C", "GPIO, ADC, PWM", "UART communication", "Basic sensors"],
#             "intermediate": ["RTOS tasks", "DMA", "Low power modes", "Embedded debugging"],
#             "expert": ["Driver development", "BSP work", "Performance optimization", "Embedded Linux basics"]
#         },
#         "projects": ["Sensor logger", "Bluetooth data system", "Motor control basic"],
#         "opportunities": ["IoT", "Automotive", "Consumer electronics"]
#     },

#     {
#         "id": "pcb-design",
#         "title": "PCB Design Engineer",
#         "domain": "Hardware",
#         "shortDescription": "Design schematics and PCB layouts ensuring signal integrity, power integrity and manufacturability.",
#         "tools": ["Altium", "KiCad", "OrCAD", "LTspice"],
#         "fundamentals": ["Analog basics", "Digital basics", "Power supply design", "EMI/EMC"],
#         "roadmap": {
#             "basic": ["Learn schematic design", "2-layer PCB", "Basic routing rules"],
#             "intermediate": ["High-speed routing basics", "Impedance", "Grounding", "Decoupling"],
#             "expert": ["DDR/SerDes layout", "SI/PI analysis", "EMC compliance design"]
#         },
#         "projects": ["ESP32 board", "STM32 dev board", "Power supply PCB"],
#         "opportunities": ["Electronics product companies", "R&D labs"]
#     },

#     {
#         "id": "rf-engineer",
#         "title": "RF Engineer",
#         "domain": "RF",
#         "shortDescription": "Design and test RF systems, antennas, matching networks and RF front-end circuits.",
#         "tools": ["ADS", "HFSS", "CST", "VNA", "Spectrum Analyzer"],
#         "fundamentals": ["Transmission lines", "S-parameters", "Smith chart", "RF measurements"],
#         "roadmap": {
#             "basic": ["Learn Smith chart", "Basic matching", "S11/S21 understanding"],
#             "intermediate": ["RF filters", "LNA/PA basics", "Antenna simulation"],
#             "expert": ["System-level RF design", "RFIC basics", "High-frequency debugging"]
#         },
#         "projects": ["Microstrip antenna", "Matching network", "RF filter design"],
#         "opportunities": ["Telecom", "Aerospace", "Defense"]
#     },

#     {
#         "id": "asic-design",
#         "title": "ASIC Design Engineer",
#         "domain": "VLSI",
#         "shortDescription": "End-to-end chip design from architecture to tapeout including RTL, verification and integration.",
#         "tools": ["SystemVerilog", "EDA tools", "Git", "Python"],
#         "fundamentals": ["Digital design", "RTL", "Verification", "Timing"],
#         "roadmap": {
#             "basic": ["Learn RTL basics", "Build small blocks"],
#             "intermediate": ["Integrate IPs", "Work with constraints", "Debug timing"],
#             "expert": ["SOC architecture", "Tapeout ownership", "Cross-team coordination"]
#         },
#         "projects": ["SOC mini-project", "Peripheral integration"],
#         "opportunities": ["Chip companies", "R&D labs"]
#     },

#     {
#         "id": "soc-integration",
#         "title": "SoC Integration Engineer",
#         "domain": "VLSI",
#         "shortDescription": "Integrate multiple IP blocks, connect buses, manage clocks/resets, and ensure system works.",
#         "tools": ["SystemVerilog", "IP-XACT", "EDA tools"],
#         "fundamentals": ["Bus protocols", "Clock/reset", "Address mapping"],
#         "roadmap": {
#             "basic": ["Learn AXI/APB basics", "Integrate simple IPs"],
#             "intermediate": ["Interrupt controllers", "DMA integration", "Debug integration issues"],
#             "expert": ["Complex SoC integration", "Low power domains", "System bring-up"]
#         },
#         "projects": ["AXI interconnect integration", "Simple SoC platform"],
#         "opportunities": ["SOC teams in semiconductor companies"]
#     },

#     {
#         "id": "ams-verification",
#         "title": "AMS Verification Engineer",
#         "domain": "VLSI",
#         "shortDescription": "Verify mixed-signal blocks using Verilog-AMS, simulations and testbenches.",
#         "tools": ["Cadence Spectre", "Verilog-AMS", "Virtuoso"],
#         "fundamentals": ["Analog circuits", "Digital design", "Mixed-signal simulation"],
#         "roadmap": {
#             "basic": ["Analog basics", "Digital basics", "Simulation basics"],
#             "intermediate": ["Mixed-signal testbench", "Behavioral modeling"],
#             "expert": ["System AMS verification", "Silicon correlation"]
#         },
#         "projects": ["ADC behavioral model", "PLL testbench"],
#         "opportunities": ["Mixed-signal companies"]
#     },

#     {
#         "id": "power-electronics",
#         "title": "Power Electronics Engineer",
#         "domain": "Core ECE",
#         "shortDescription": "Design converters (buck/boost), inverters, motor drives and power control systems.",
#         "tools": ["MATLAB", "Simulink", "PSIM", "LTspice"],
#         "fundamentals": ["Power devices", "Converters", "Control systems", "PWM"],
#         "roadmap": {
#             "basic": ["Rectifiers, buck/boost basics", "MOSFET/IGBT basics"],
#             "intermediate": ["Closed loop control", "Motor drives", "Thermal basics"],
#             "expert": ["High power systems", "EV powertrain", "EMI compliance"]
#         },
#         "projects": ["Buck converter", "Inverter simulation", "BLDC control"],
#         "opportunities": ["EV", "Energy sector", "Industrial automation"]
#     },

#     {
#         "id": "iot-engineer",
#         "title": "IoT Engineer",
#         "domain": "Embedded + Software",
#         "shortDescription": "Build IoT systems with sensors, connectivity, cloud integration and dashboards.",
#         "tools": ["ESP32", "MQTT", "Node.js", "Python", "Firebase", "AWS IoT"],
#         "fundamentals": ["Networking basics", "Sensors", "Embedded basics", "Cloud basics"],
#         "roadmap": {
#             "basic": ["ESP32 basics", "MQTT publish/subscribe", "Simple dashboard"],
#             "intermediate": ["Cloud integration", "Database", "OTA updates"],
#             "expert": ["Security", "Scalable architecture", "Edge AI"]
#         },
#         "projects": ["Smart home sensor", "Weather station", "Asset tracking"],
#         "opportunities": ["IoT startups", "Product companies"]
#     },

#     {
#         "id": "robotics-engineer",
#         "title": "Robotics Engineer",
#         "domain": "Robotics",
#         "shortDescription": "Build robots using sensors, control, perception and ROS-based software.",
#         "tools": ["ROS2", "Python", "C++", "Gazebo", "OpenCV"],
#         "fundamentals": ["Control systems", "Kinematics", "Sensors", "SLAM basics"],
#         "roadmap": {
#             "basic": ["Learn ROS basics", "Motor control basics", "Sensor integration"],
#             "intermediate": ["SLAM basics", "Path planning", "Computer vision basics"],
#             "expert": ["Autonomous navigation", "Multi-sensor fusion", "Real robot deployment"]
#         },
#         "projects": ["Line follower robot", "Obstacle avoidance", "Mini SLAM robot"],
#         "opportunities": ["Robotics companies", "Research labs"]
#     },

#     {
#         "id": "automation-plc",
#         "title": "Automation / PLC Engineer",
#         "domain": "Industrial",
#         "shortDescription": "Work with PLCs, SCADA, industrial sensors and automation systems.",
#         "tools": ["Siemens TIA Portal", "Allen Bradley", "SCADA"],
#         "fundamentals": ["Control basics", "Sensors", "Industrial communication"],
#         "roadmap": {
#             "basic": ["PLC ladder logic basics", "Basic sensors & relays"],
#             "intermediate": ["SCADA integration", "Industrial protocols (Modbus)"],
#             "expert": ["Plant-level automation", "Safety systems", "Optimization"]
#         },
#         "projects": ["Conveyor automation", "Tank level control"],
#         "opportunities": ["Manufacturing plants", "Automation companies"]
#     },

#     {
#         "id": "signal-processing",
#         "title": "DSP Engineer (Signal Processing)",
#         "domain": "DSP",
#         "shortDescription": "Develop algorithms for filtering, FFT, audio/image processing and real-time DSP systems.",
#         "tools": ["MATLAB", "Python", "C", "DSP processors"],
#         "fundamentals": ["Signals & Systems", "Fourier transforms", "Filters", "Sampling"],
#         "roadmap": {
#             "basic": ["Learn FFT", "FIR/IIR basics", "MATLAB DSP practice"],
#             "intermediate": ["Adaptive filters", "Real-time implementation", "Optimization in C"],
#             "expert": ["Advanced DSP", "Hardware acceleration", "Research-level work"]
#         },
#         "projects": ["Noise reduction", "Audio equalizer", "ECG filtering"],
#         "opportunities": ["Audio", "Medical devices", "Radar/Defense"]
#     },

#     {
#         "id": "antenna-engineer",
#         "title": "Antenna Design Engineer",
#         "domain": "RF",
#         "shortDescription": "Design and optimize antennas for wireless, satellite and radar applications.",
#         "tools": ["HFSS", "CST", "MATLAB"],
#         "fundamentals": ["EM theory", "Radiation patterns", "Impedance matching"],
#         "roadmap": {
#             "basic": ["Microstrip patch basics", "S11, VSWR"],
#             "intermediate": ["Antenna arrays", "Bandwidth improvement"],
#             "expert": ["MIMO antennas", "mmWave antennas", "Optimization algorithms"]
#         },
#         "projects": ["Patch antenna", "Yagi antenna", "Array design"],
#         "opportunities": ["Telecom", "Defense", "Satellite companies"]
#     },

#     {
#         "id": "network-engineer",
#         "title": "Network Engineer",
#         "domain": "Networking",
#         "shortDescription": "Work on routing, switching, network security and enterprise network systems.",
#         "tools": ["Cisco Packet Tracer", "Wireshark", "Linux"],
#         "fundamentals": ["OSI model", "TCP/IP", "Routing", "Subnetting"],
#         "roadmap": {
#             "basic": ["Learn IP addressing", "Switching basics", "Routing basics"],
#             "intermediate": ["CCNA level", "Network troubleshooting", "Firewalls basics"],
#             "expert": ["Enterprise architecture", "Cloud networking", "Security hardening"]
#         },
#         "projects": ["Small enterprise network design", "Wireshark analysis"],
#         "opportunities": ["IT companies", "Network service providers"]
#     },

#     {
#         "id": "semiconductor-process",
#         "title": "Semiconductor Process Engineer",
#         "domain": "Semiconductor",
#         "shortDescription": "Work on wafer fabrication, process optimization, yield improvement and quality.",
#         "tools": ["Process tools", "SPC tools", "Excel", "Data analysis"],
#         "fundamentals": ["Semiconductor physics", "Fabrication steps", "Yield"],
#         "roadmap": {
#             "basic": ["Learn fabrication flow", "Cleanroom basics"],
#             "intermediate": ["Process characterization", "Yield analysis"],
#             "expert": ["Advanced node processes", "Defect reduction", "Process ownership"]
#         },
#         "projects": ["Yield analysis case study"],
#         "opportunities": ["Foundries", "Semiconductor manufacturing"]
#     },

#     {
#         "id": "test-validation",
#         "title": "Hardware Test / Validation Engineer",
#         "domain": "Hardware",
#         "shortDescription": "Validate hardware boards and chips, run tests, debug failures and automate test setups.",
#         "tools": ["Oscilloscope", "Logic Analyzer", "Python automation"],
#         "fundamentals": ["Electronics basics", "Measurements", "Debugging"],
#         "roadmap": {
#             "basic": ["Learn measurement tools", "Basic debugging"],
#             "intermediate": ["Automated testing", "Reliability testing"],
#             "expert": ["Test strategy ownership", "Failure analysis leadership"]
#         },
#         "projects": ["Board bring-up testing", "Automated test scripts"],
#         "opportunities": ["Product companies", "Hardware labs"]
#     },

    # {
    #     "id": "eda-engineer",
    #     "title": "EDA Engineer / CAD Engineer",
    #     "domain": "VLSI",
    #     "shortDescription": "Develop scripts/tools and automate flows in VLSI using Python/TCL and EDA tools.",
    #     "tools": ["Python", "TCL", "Linux", "EDA tools"],
    #     "fundamentals": ["Scripting", "VLSI flow", "]()

# ===================
# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import json
# import os

# app = Flask(__name__)
# CORS(app)

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# DATA_PATH = os.path.join(BASE_DIR, "data", "roles.json")

# def load_roles():
#     with open(DATA_PATH, "r", encoding="utf-8") as f:
#         return json.load(f)

# @app.get("/")
# def home():
#     return jsonify({
#         "message": "ECE Roadmap Backend is running",
#         "endpoints": ["/api/roles", "/api/roles/<id>"]
#     })

# @app.get("/api/roles")
# def get_roles():
#     roles = load_roles()

#     q = request.args.get("q", "").strip().lower()
#     domain = request.args.get("domain", "").strip().lower()

#     filtered = roles

#     if q:
#         filtered = [
#             r for r in filtered
#             if q in r["title"].lower()
#             or q in r["domain"].lower()
#             or any(q in t.lower() for t in r.get("tags", []))
#         ]

#     if domain:
#         filtered = [r for r in filtered if r["domain"].lower() == domain]

#     return jsonify(filtered)

# @app.get("/api/roles/<role_id>")
# def get_role_by_id(role_id):
#     roles = load_roles()
#     for r in roles:
#         if r["id"] == role_id:
#             return jsonify(r)
#     return jsonify({"error": "Role not found"}), 404

# if __name__ == "__main__":
#     app.run(debug=True)
