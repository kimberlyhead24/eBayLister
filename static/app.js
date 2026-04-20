// ============================================================
// UPLOAD SCREEN - Photo preview and drag/drop
// ============================================================

const fileInput = document.getElementById("file-input");
const previewGrid = document.getElementById("preview-grid");
const photoCount = document.getElementById("photo-count");
const countNumber = document.getElementById("count-number");
const dropZone = document.getElementById("drop-zone");
const generateBtn = document.getElementById("generate-draft-btn");
const uploadError = document.getElementById("upload-error");

if (fileInput && previewGrid) {
  fileInput.addEventListener("change", () => {
    renderPreviews(Array.from(fileInput.files));
  });
}

function renderPreviews(files) {
  previewGrid.innerHTML = "";

  files.forEach((file, index) => {
    const reader = new FileReader();
    reader.onload = (e) => {
      const card = document.createElement("div");
      card.className =
        "relative group bg-slate-100 rounded-lg border aspect-square overflow-hidden";
      card.innerHTML = `
        <img src="${e.target.result}" class="object-cover w-full h-full" />
        <div class="absolute top-1 left-1 px-1 rounded text-white text-[10px] font-bold
          ${index === 0 ? "bg-blue-600" : "bg-black/50"}">
          ${index === 0 ? "Main" : index + 1}
        </div>
        <button
          class="absolute top-1 right-1 bg-red-500 text-white rounded-full w-5 h-5
            flex items-center justify-center text-xs opacity-0 group-hover:opacity-100
            transition-opacity"
          onclick="this.closest('.relative').remove(); updateCount();"
        >&times;</button>
      `;
      previewGrid.appendChild(card);
      updateCount();
    };
    reader.readAsDataURL(file);
  });
}

function updateCount() {
  const total = previewGrid.querySelectorAll(".relative").length;
  if (photoCount && countNumber) {
    countNumber.textContent = total;
    photoCount.classList.toggle("hidden", total === 0);
  }
}

// Drag and drop
if (dropZone) {
  ["dragenter", "dragover"].forEach((name) => {
    dropZone.addEventListener(name, (e) => {
      e.preventDefault();
      dropZone.classList.add("border-blue-500", "bg-blue-50");
    });
  });

  ["dragleave", "drop"].forEach((name) => {
    dropZone.addEventListener(name, (e) => {
      e.preventDefault();
      dropZone.classList.remove("border-blue-500", "bg-blue-50");
    });
  });

  dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    const files = Array.from(e.dataTransfer.files).filter((f) =>
      f.type.startsWith("image/")
    );
    renderPreviews(files);
  });
}

// Generate draft button
if (generateBtn) {
  generateBtn.addEventListener("click", async () => {
    clearError();

    const files = fileInput ? Array.from(fileInput.files) : [];
    if (files.length === 0) {
      showError("Please upload at least one photo before generating a draft.");
      return;
    }

    generateBtn.textContent = "Generating Draft...";
    generateBtn.disabled = true;

    const formData = new FormData();
    files.forEach((file) => formData.append("files", file));

    const sellerNotes = document.getElementById("seller-notes");
    if (sellerNotes) formData.append("seller_notes", sellerNotes.value);

    const itemHint = document.getElementById("item-hint");
    if (itemHint) formData.append("item_hint", itemHint.value);

    const condition = document.getElementById("condition-hint");
    if (condition) formData.append("condition_hint", condition.value);

    const msrp = document.getElementById("msrp-hint");
    if (msrp) formData.append("msrp", msrp.value);

    const listingType = document.getElementById("listing-type");
    if (listingType) formData.append("listing_type", listingType.value);

    const quantity = document.getElementById("quantity");
    if (quantity) formData.append("quantity", quantity.value);

    const shipping = document.getElementById("shipping-carrier");
    if (shipping) formData.append("shipping_carrier", shipping.value);

    const offers = document.getElementById("allow-offers");
    if (offers) formData.append("allow_offers", offers.value);

    try {
      const response = await fetch("/upload-photos", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const err = await response.json();
        showError("Error: " + (err.detail || "Something went wrong."));
        generateBtn.textContent = "Generate Draft with AI →";
        generateBtn.disabled = false;
        return;
      }

      const data = await response.json();
      window.location.href = `/review/${data.draft_id}`;
    } catch (err) {
      showError("Network error. Please check the server is running.");
      generateBtn.textContent = "Generate Draft with AI →";
      generateBtn.disabled = false;
    }
  });
}

// ============================================================
// REVIEW SCREEN
// ============================================================

const titleInput = document.getElementById("listing-title");
const titleCharCount = document.getElementById("title-char-count");

if (titleInput && titleCharCount) {
  function updateCharCount() {
    const len = titleInput.value.length;
    titleCharCount.textContent = `${len} / 80 characters`;
    titleCharCount.style.color = len > 70 ? "#dc2626" : "#94a3b8";
  }
  titleInput.addEventListener("input", updateCharCount);
  updateCharCount();
}

// Listing type toggle — hide quantity if auction
const listingTypeSelect = document.getElementById("listing-type");
const quantityField = document.getElementById("listing-quantity");

if (listingTypeSelect && quantityField) {
  listingTypeSelect.addEventListener("change", () => {
    if (listingTypeSelect.value === "auction") {
      quantityField.value = "1";
      quantityField.disabled = true;
      quantityField.classList.add("opacity-50");
    } else {
      quantityField.disabled = false;
      quantityField.classList.remove("opacity-50");
    }
  });
}

// Save draft button
const saveDraftBtn = document.getElementById("save-draft-btn");
if (saveDraftBtn) {
  saveDraftBtn.addEventListener("click", () => {
    saveDraftBtn.textContent = "Saved";
    saveDraftBtn.classList.add("text-green-600");
    setTimeout(() => {
      saveDraftBtn.textContent = "Save Draft";
      saveDraftBtn.classList.remove("text-green-600");
    }, 2000);
  });
}

// Approve button
const approveBtn = document.getElementById("approve-btn");
if (approveBtn) {
  approveBtn.addEventListener("click", () => {
    const badge = document.querySelector(".bg-amber-100");
    if (badge) {
      badge.textContent = "approved";
      badge.className =
        "px-3 py-1 bg-green-100 text-green-800 text-xs font-bold rounded-full uppercase";
    }
    approveBtn.textContent = "Approved";
    approveBtn.disabled = true;
    approveBtn.classList.replace("bg-blue-600", "bg-green-600");
  });
}

// Reject button
const rejectBtn = document.getElementById("reject-btn");
if (rejectBtn) {
  rejectBtn.addEventListener("click", () => {
    const badge = document.querySelector(".bg-amber-100");
    if (badge) {
      badge.textContent = "rejected";
      badge.className =
        "px-3 py-1 bg-red-100 text-red-800 text-xs font-bold rounded-full uppercase";
    }
  });
}

// Publish button
const publishBtn = document.getElementById("publish-btn");
if (publishBtn) {
  publishBtn.addEventListener("click", () => {
    publishBtn.textContent = "Publishing...";
    publishBtn.disabled = true;
    setTimeout(() => {
      publishBtn.textContent = "Published to eBay ✓";
      publishBtn.classList.replace("bg-green-600", "bg-slate-400");
    }, 1500);
  });
}