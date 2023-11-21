const elDragLists = document.querySelectorAll(".drag-list"); // ul
const elDragItems = document.querySelectorAll(".drag-item"); // li

let draggedItem = null;

for (let i = 0; i < elDragItems.length; i++) {
	const item = elDragItems[i];

	item.addEventListener("dragstart", function () {
		draggedItem = item;
		setTimeout(function () {
			item.style.display = "none";
		}, 0);
	});

	item.addEventListener("dragend", function () {
		setTimeout(() => {
			item.style.display = "block";
			draggedItem = null;
		}, 0);
	});

	for (let j = 0; j < elDragLists.length; j++) {
		const list = elDragLists[j];

		list.addEventListener("dragover", function (evt) {
			evt.preventDefault();
		});

		list.addEventListener("dragenter", function (evt) {
			evt.preventDefault();
		});

		list.addEventListener("drop", function () {
			this.append(draggedItem);
		});
	}
}
