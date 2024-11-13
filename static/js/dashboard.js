const BASE_URL = "http://localhost:5000/api";

let isLoading = false;

async function getData() {
    const maleCount = { key: "male", value: 0 };
    const femaleCount = { key: "female", value: 0 };
    const ageCounts = {
        "2-16": 0,
        "17-30": 0,
        "31-45": 0,
        "46-65": 0,
        "65+": 0,
    };
    const raceCounts = {
        White: 0,
        Black: 0,
        Asian: 0,
        Other: 0,
    };

    try {
        isLoading = true;
        document.getElementById("loading").classList.remove("hidden");

        const patientData = await axios.get(`${BASE_URL}/patient`);
        const patients = patientData.data;

        console.log(patients)

        patients.forEach((entry) => {
            const gender = entry.GENDER ?? "unspecified";
            if (gender === "M") {
                maleCount.value++;
            } else if (gender === "F") {
                femaleCount.value++;
            }

            const birthYear = entry.BIRTHDATE ? parseInt(entry.BIRTHDATE.slice(0, 4)) : undefined;
            const race = entry.RACE;

            if (birthYear) {
                const age = 2024 - birthYear;
                if (age <= 16) ageCounts["2-16"]++;
                else if (age <= 30) ageCounts["17-30"]++;
                else if (age <= 45) ageCounts["31-45"]++;
                else if (age <= 65) ageCounts["46-65"]++;
                else ageCounts["65+"]++;
            }

            if (race === "white") raceCounts["White"]++;
            else if (race === "black") raceCounts["Black"]++;
            else if (race === "asian") raceCounts["Asian"]++;
            else raceCounts["Other"]++;
        });

        const practitionerData = await axios.get(`${BASE_URL}/provider`);
        const practitionerCount = practitionerData.data.data.providers.length;

        const maxAgeRange = Object.entries(ageCounts).reduce((max, current) => {
            return current[1] > max[1] ? current : max;
        }, ["", 0])[0];

        updateUI({
            maleCount: (maleCount.value / patients.length) * 100,
            femaleCount: (femaleCount.value / patients.length) * 100,
            totalPatients: patients.length,
            popularMedication: "",  // Placeholder, can be updated as needed
            maxAgeRange,
            practitionerCount,
            ageData: Object.entries(ageCounts),
            raceData: Object.entries(raceCounts),
        });

    } catch (error) {
        console.error(error);
    } finally {
        isLoading = false;
        document.getElementById("loading").classList.add("hidden");
    }
}

function updateUI({
    maleCount,
    femaleCount,
    totalPatients,
    popularMedication,
    maxAgeRange,
    practitionerCount,
    ageData,
    raceData,
}) {
    // Update Card Data Stats
    const cardContainer = document.getElementById("content");
    cardContainer.innerHTML = `

<div class="grid-cols-4 mb-8 grid gap-4">
    <div
        class="rounded-sm border border-stroke bg-white px-7.5 py-6 shadow-default dark:border-strokedark dark:bg-boxdark">
        <div class="flex h-11.5 w-11.5 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4">
            <svg class="text-primary" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none"
                stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"
                class="lucide lucide-users">
                <path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2" />
                <circle cx="9" cy="7" r="4" />
                <path d="M22 21v-2a4 4 0 0 0-3-3.87" />
                <path d="M16 3.13a4 4 0 0 1 0 7.75" />
            </svg>
        </div>

        <div class="mt-4 flex items-end justify-between">
            <div>
                <h4 class="text-title-md font-bold text-black dark:text-white">
                    ${totalPatients}
                </h4>
                <span class="text-sm font-medium">Total Patients</span>
            </div>
        </div>
    </div>

    <div
        class="rounded-sm border border-stroke bg-white px-7.5 py-6 shadow-default dark:border-strokedark dark:bg-boxdark">
        <div class="flex h-11.5 w-11.5 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4">
            <svg class="text-primary" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-pill"><path d="m10.5 20.5 10-10a4.95 4.95 0 1 0-7-7l-10 10a4.95 4.95 0 1 0 7 7Z"/><path d="m8.5 8.5 7 7"/></svg>
        </div>

        <div class="mt-4 flex items-end justify-between">
            <div>
                <h4 class="text-title-md font-bold text-black dark:text-white">
                    ${popularMedication || "Paracetamol"}
                </h4>
                <span class="text-sm font-medium">Most Prescribed Medication</span>
            </div>
        </div>
    </div>

    <div
        class="rounded-sm border border-stroke bg-white px-7.5 py-6 shadow-default dark:border-strokedark dark:bg-boxdark">
        <div class="flex h-11.5 w-11.5 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4">
            <svg class="text-primary" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-user-round"><circle cx="12" cy="8" r="5"/><path d="M20 21a8 8 0 0 0-16 0"/></svg>
        </div>

        <div class="mt-4 flex items-end justify-between">
            <div>
                <h4 class="text-title-md font-bold text-black dark:text-white">
                    ${maxAgeRange}
                </h4>
                <span class="text-sm font-medium">Majority Age Group</span>
            </div>
        </div>
    </div>

    <div
        class="rounded-sm border border-stroke bg-white px-7.5 py-6 shadow-default dark:border-strokedark dark:bg-boxdark">
        <div class="flex h-11.5 w-11.5 items-center justify-center rounded-full bg-meta-2 dark:bg-meta-4">
            <svg class="text-primary" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-stethoscope"><path d="M11 2v2"/><path d="M5 2v2"/><path d="M5 3H4a2 2 0 0 0-2 2v4a6 6 0 0 0 12 0V5a2 2 0 0 0-2-2h-1"/><path d="M8 15a6 6 0 0 0 12 0v-3"/><circle cx="20" cy="10" r="2"/></svg>
        </div>

        <div class="mt-4 flex items-end justify-between">
            <div>
                <h4 class="text-title-md font-bold text-black dark:text-white">
                    ${practitionerCount}
                </h4>
                <span class="text-sm font-medium">Total Practitioners</span>
            </div>
        </div>
    </div>
</div>
`;

    // Update Charts
    const chartsContainer = document.getElementById("charts");
    //     chartsContainer.innerHTML = `
    // <div class="col-span-12 rounded-sm border bg-white px-5 pb-5 pt-7.5 shadow-default">
    //     <h5>Gender Distribution (Patients)</h5>
    //     <div id="chart-three"></div>
    // </div>
    // `;

    renderDonutChart('chart-three', [{ value: maleCount }, { value: femaleCount }]);
}

function renderDonutChart(containerId, data) {
    const svg = d3.select(`#${containerId}`).append('svg').attr('width', 200).attr('height', 200);
    const radius = 100;
    const color = d3.scaleOrdinal(['#FFC0CB', '#3C50E0']);
    const pie = d3.pie().value(d => d.value);

    const arc = d3.arc().innerRadius(60).outerRadius(100);
    const g = svg.selectAll('.arc')
        .data(pie(data))
        .enter().append('g')
        .attr('class', 'arc')
        .attr('transform', 'translate(100,100)');

    g.append('path')
        .attr('d', arc)
        .style('fill', (d, i) => color(i));
}

getData();
