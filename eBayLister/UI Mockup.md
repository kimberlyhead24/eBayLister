## UI Design: Two-Screen eBay Listing App

This design covers:

- Screen 1: Capture multiple photos of an item
- Screen 2: Fully filled-out eBay posting form that can be edited/refined

The goal is a smooth, guided flow from photos to a complete listing with editable fields, live previews, and easy publishing/export options.

---

## Screen 1: Photo Capture & Management

### Key Goals

- Quick photo capture (camera or gallery)
- Clear feedback on photo count and quality
- Easy reordering, editing, and deletion
- Prepare metadata (title, condition hints) from photos

### Layout

- **Header**
    
    - Title: “Add Item Photos”
    
    
- **Photo Capture Area**
    
    - Large camera/viewfinder tile with capture button
    - Thumbnail strip below for:
        - Existing photos (horizontal scroll)
        - Reorder handles (drag-and-drop)
        - Delete button (trash icon)
    - Quick actions:
        - “Add Photo” (camera roll or take photo)
        - “Auto-Enhance” (optional basic image adjustments)
- **Photo Slots / Grid**
    
    - Support up to N photos (e.g., 10 photos)
    - Each photo thumbnail shows:
        - Small crop/edit icon
        - Tap to view full-size
    - Drag to reorder (pointer handle)
- **Metadata Helpers (optional panel)**
    
    - Auto-extract hints from photos:
        - Example: if a model number is visible, suggest including it in title
    - Quick fields:
        - Suggested Title snippet (read-only or editable)
- **Footer / Actions**
    
    - Primary: “Continue to Listing” (disabled until at least 1 photo)
    - Secondary: “Save Draft” / “Cancel”

### Data & Interactions

- Photo objects:
    
    ```
    { id, uri, order, ratingQuality, metadataHints[] }
    ```
    
- On add: open camera or gallery, push new photo with next order
- On reorder: update
    
    ```
    order
    ```
    
    values
- On delete: remove photo, reorder remaining
- On continue: pass photo array to Screen 2 via navigation state

### Accessibility & UX

- High-contrast controls, large tap targets
- Alt text/captions for screenshots
- Keyboard navigation support for reordering (where feasible)

---

## Screen 2: Fully Filled-out eBay Listing Form (Editable)

### Key Goals

- Pre-fill with data gathered from photos and sensible defaults
- Comprehensive, but still approachable: title, category, condition, pricing, shipping, description, photos, etc.
- Live preview pane to the side or below the form
- Save as draft, publish, or export to a file

### Layout

- **Header**
    
    - Title: “Create Your eBay Listing”
    - Progress indicator: Screen 2 of 2
    - Back button to Screen 1
    - Quick actions: Save Draft, Publish (or Continue to Platform)
- **Two-Column Layout (Responsive)**
    
    - Left Column: Form Fields
    - Right Column: Live Preview (WYSIWYG) plus photo gallery
- **Form Fields (Grouped)**
    
    - **Item Details**
        - ```
            Title
            ```
            
            (text)
        - ```
            Subtitle
            ```
            
            (optional)
        - ```
            Category
            ```
            
            (dropdown with search)
        - ```
            Brand
            ```
            
            (text)
        - ```
            Model/MPN
            ```
            
            (text)
        - ```
            Condition
            ```
            
            (dropdown: New, New with tags, Used, Refurbished)
        - ```
            UPC/EAN
            ```
            
            (text)
    - **Photos**
        - Gallery strip (from Screen 1) with reordering and replacement
    - **Pricing & Shipping**
        - ```
            Starting Price
            ```
            
            (number)
        - ```
            Buy It Now
            ```
            
            (optional)
        - ```
            Reserve Price
            ```
            
            (optional)
        - ```
            Best Offer
            ```
            
            (toggle)
        - ```
            Shipping Cost
            ```
            
            (flat rate / calculated)
        - ```
            Shipping Policy
            ```
            
            (text)
        - ```
            Handling Time
            ```
            
            (dropdown)
    - **Item Description**
        - Rich text editor (bold, bullets, links)
        - Image placeholders or inline image blocks
    - **Item Specifics**
        - Customizable fields based on category (e.g., size, color, material)
    - **Seller Details (optional)**
        - ```
            Return Policy
            ```
            
            (text)
        - ```
            Payment Methods
            ```
            
            (checkboxes)
    - **Listing Options**
        - ```
            Visibility
            ```
            
            (Public, Hidden)
        - ```
            Duration
            ```
            
            (3, 5, 7, 10, 30 days)
    - **SEO & Social**
        - ```
            Search Keywords
            ```
            
            (tags)
        - ```
            Listing Tags
            ```
            
            (optional)
    - **Legal & Compliance**
        - Display a reminder to comply with platform policies
- **Live Preview Pane**
    
    - Mimics eBay listing page:
        - Title, photos, price, shipping, location
        - Description block with formatting
        - Category and item specifics
    - Inline edit indicators:
        - If a field in the form changes, the preview updates in real time
    - Share/Export:
        - Copy listing data as JSON
        - Export to draft file or clipboard
        - Preview mobile view
- **Footer / Actions**
    
    - Primary: “Save Draft” and “Publish Listing” (or “List Now”)
    - Secondary: “Reset Form” (clear to defaults)
    - Validation indicators: highlight missing required fields

### Data Model (Draft)

- ```
    ListingDraft
    ```
    
    :
    - ```
        photos: [ { id, uri, order } ]
        ```
        
    - ```
        title, category, brand, model, condition, upc/ean
        ```
        
    - ```
        pricing: { startingPrice, buyItNow, bestOffer, reservePrice }
        ```
        
    - ```
        shipping: { cost, policy, handlingTime }
        ```
        
    - ```
        description: richText
        ```
        
        (could be HTML or structured blocks)
    - ```
        itemSpecifics: { key: value }
        ```
        
    - ```
        returnPolicy, paymentMethods, visibility, duration
        ```
        
    - ```
        keywords: [string]
        ```
        
    - ```
        metadataHints
        ```
        
        (from Screen 1)
- On save: persist to local storage or backend
- On publish: trigger platform API or export data for submission

### Interactions & UX Details

- Auto-fill suggestions:
    - If photos contain a brand/model, suggest pre-filling fields
    - Category-specific specifics adapt based on selection
- Validation:
    - Required: title, category, photos (Screen 1), price
    - Warnings for potentially missing policy details (optional but recommended)
- Rich Text Editor:
    - Basic formatting: bold, italic, lists, links
    - Image blocks within description (optional)
- Accessibility:
    - Screen reader-friendly labels, proper aria attributes
    - Keyboard shortcuts for common actions (e.g., Ctrl/Cmd+S to save)

---

## Interaction Flow Summary

1. User launches the app and lands on Screen 1.
2. User captures multiple photos, reorders, deletes, and confirms at least one photo.
3. User taps “Continue to Listing” to move to Screen 2.
4. Screen 2 loads with auto-filled fields and a live preview.
5. User edits any field, sees live updates in the preview, adds details to description and item specifics.
6. User can Save Draft, Publish Listing, or Export data. If publishing, confirm actions per platform requirements.

---

## Example Tech Skeleton (React-like)

Below is a lightweight, high-level structure you could adapt to React, React Native, or Flutter. It focuses on state and component organization rather than full implementation.

### Components

- ```
    PhotoScannerScreen
    ```
    
    - Props:
        
        ```
        onNext(listingPhotos)
        ```
        
    - State:
        
        ```
        photos: Photo[]
        ```
        
    - Handlers:
        
        ```
        addPhoto
        ```
        
        ,
        
        ```
        removePhoto
        ```
        
        ,
        
        ```
        reorderPhotos
        ```
        
        ,
        
        ```
        openEditorForPhoto
        ```
        
- ```
    ListingEditorScreen
    ```
    
    - Props:
        
        ```
        initialDraft
        ```
        
        ,
        
        ```
        onPublish(draft)
        ```
        
    - State:
        
        ```
        draft: ListingDraft
        ```
        
    - Subcomponents:
        
        ```
        TextInput
        ```
        
        ,
        
        ```
        Dropdown
        ```
        
        ,
        
        ```
        RichTextEditor
        ```
        
        ,
        
        ```
        PhotoGallery
        ```
        
        ,
        
        ```
        LivePreview
        ```
        
    - Handlers:
        
        ```
        updateField
        ```
        
        ,
        
        ```
        updateDescription
        ```
        
        ,
        
        ```
        validate
        ```
        
        ,
        
        ```
        saveDraft
        ```
        
        ,
        
        ```
        publish
        ```
        

### Data Models (TypeScript-like)

```ts
type Photo = {
  id: string;
  uri: string;
  order: number;
};

type PriceInfo = {
  startingPrice: number;
  buyItNow?: number;
  bestOffer?: boolean;
  reservePrice?: number;
};

type ShippingInfo = {
  cost: number;
  policy?: string;
  handlingTime?: string;
};

type ListingDraft = {
  photos: Photo[];
  title: string;
  category: string;
  brand?: string;
  model?: string;
  condition: 'New' | 'New with tags' | 'Used' | 'Refurbished';
  upc?: string;
  price: PriceInfo;
  shipping: ShippingInfo;
  description: string; // Rich text / HTML
  itemSpecifics: Record<string, string>;
  returnPolicy?: string;
  paymentMethods?: string[];
  visibility: 'Public' | 'Hidden';
  duration: number; // days
  keywords?: string[];
};
```

---

## Best Practices & Tips

- Start simple: let Screen 1 focus on fast photo capture; Screen 2 handles most data.
- Use live preview to reduce back-and-forth edits.
- Provide sensible defaults and auto-suggestions to speed up listing creation.
- Include autosave functionality to prevent data loss.
- Ensure the UI scales well on mobile devices, where listing creation often happens.