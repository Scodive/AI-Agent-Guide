document.addEventListener("DOMContentLoaded", () => {
  const table = document.getElementById("paper-table");
  if (!table) return;
  const rows = Array.from(table.querySelectorAll("tbody tr"));
  const search = document.getElementById("paper-search");
  const topic = document.getElementById("paper-topic");
  const year = document.getElementById("paper-year");
  const type = document.getElementById("paper-type");
  const count = document.getElementById("paper-count");
  const normalize = value => value.toLocaleLowerCase().trim();
  const filter = () => {
    const query = normalize(search.value);
    let visible = 0;
    rows.forEach(row => {
      const matches = (!query || normalize(row.textContent).includes(query)) &&
        (!topic.value || row.dataset.topic === topic.value) &&
        (!year.value || row.dataset.year === year.value) &&
        (!type.value || row.dataset.type === type.value);
      row.hidden = !matches;
      if (matches) visible += 1;
    });
    count.textContent = `显示 ${visible} / ${rows.length} 篇`;
  };
  [search, topic, year, type].forEach(control => control.addEventListener("input", filter));
});
