# Obsidian Nix Packages

All Obsidian community plugins and themes packaged as Nix derivations, sourced from
[obsidianmd/obsidian-releases](https://github.com/obsidianmd/obsidian-releases).

## Usage

Add this flake as an input and reference packages by their **Package ID**:

```nix
inputs.obsidian-nix.url = "github:soulvice/obsidian-nix";

# then inside your config:
inputs.obsidian-nix.packages.${system}.dataview
inputs.obsidian-nix.packages.${system}.catppuccin
```

---

## Plugins (2725)

| Name | Package ID | Description |
|------|-----------|-------------|
| [.md Merge](https://github.com/tosatur/obsidian-md-merge) | `md-merge` | Merge all markdown files from a folder into a single file. |
| [.url WebView Opener](https://github.com/Kieirra/obsidian-url-extension) | `url-webview-opener` | Opens .url files in the internal webview. |
| [13th Age Statblocks](https://github.com/ben/obsidian-13th-age-statblocks) | `13th-age-statblocks` | Render 13th Age statblocks in Obsidian. |
| [2Hop Links Plugin](https://github.com/tokuhirom/obsidian-2hop-links-plugin) | `obsidian-2hop-links-plugin` | Add links to other pages at the bottom of the editor. |
| [2Hop Links Plus](https://github.com/L7Cy/obsidian-2hop-links-plus) | `2hop-links-plus` | Related links up to 2 hops away are displayed in a card format, allowing for easy browsing through connections between notes. Each card contains a preview of the corresponding note. |
| [3D Graph](https://github.com/AlexW00/obsidian-3d-graph) | `3d-graph` | A 3D Graph for Obsidian |
| [3D Graph New](https://github.com/HananoshikaYomaru/obsidian-3d-graph) | `3d-graph-new` | A 3D Graph for Obsidian |
| [@ Symbol Linking](https://github.com/Ebonsignori/obsidian-at-symbol-linking) | `at-symbol-linking` | Adds ability to link with @ (the At Symbol) in Obsidian. Can limit @ linking to specific folders e.g. People/ |
| [Abbreviations and Acronyms](https://github.com/dragonish/obsidian-abbreviations) | `abbreviations-mark` | Implements automatic marking of abbreviations and acronyms (terminology). |
| [Abbreviations expander](https://github.com/WoodenMaiden/obsidian-abbreviations) | `abbreviations` | Easily create abbreviations that will be expanded after hitting `Space`. |
| [Abbrlink](https://github.com/Hoshino-Yumetsuki/obsidian-plugin-abbrlink) | `abbrlink` | Automatically generate permanent short links for your markdown files. |
| [ABC Music Notation](https://github.com/abcjs-music/obsidian-plugin-abcjs) | `music-code-blocks` | Obsidian plugin which renders ABC music notation from code blocks using the `abc` language specifier. |
| [About Blank](https://github.com/Ai-Jani/about-blank) | `about-blank` | Customize the empty file (New tab) itself a little bit by adding "Commands" or "Open files". And edit these: Grouping, Set icon, Ask before execution, Register as a new command. |
| [Account Linker](https://github.com/qwegat/Obsidian-Account-Linker) | `obsidian-account-linker` | Plugin for describing external service accounts in the front matter |
| [Account Viewer](https://github.com/muaz742/obsidian-accointing-viewer) | `account-viewer` | Automatically generate accounting tables from Markdown code blocks tagged with accounting. |
| [Accounting Journal and Ledger](https://github.com/JavierRibaldelRio/accounting-journal-ledger) | `accounting-journal-ledger` | Tool for recording simple journal entries in class, based on the Spanish libro diario and libro mayor (ledger). Uses double-entry bookkeeping (Not a full accounting system). |
| [Ace Code Editor](https://github.com/Raven-Pensieve/obsidian-ace-code-editor) | `ace-code-editor` | An enhanced code editor using Ace editor, providing syntax highlighting, code folding, and other advanced editing features. |
| [Achievements](https://github.com/Zachatoo/obsidian-achievements) | `obsidian-achievements` | Add achievements to Obsidian. |
| [Actions URI](https://github.com/czottmann/obsidian-actions-uri) | `actions-uri` | Adds additional `x-callback-url` endpoints to the app for common actions — it's a clean, super-charged addition to Obsidian URI. |
| [Activity Heatmap](https://github.com/zakhij/obsidian-activity-heatmap) | `activity-heatmap` | Tracks and visualizes app activity, similar to GitHub's contribution chart. |
| [Activity Logger](https://github.com/Creling/obsidian-activity-logger) | `obsidian-activity-logger` | Log your activities like creating notes, modifying notes, deleting notes and so on. |
| [ActivityWatch](https://github.com/LordGrimmauld/aw-watcher-obsidian) | `aw-watcher-obsidian` | This is a plugin bridging compatibility between ActivityWatch and Obsidian. |
| [Adamantine Pick](https://github.com/notlibrary/obsidian-adamantine-pick) | `adamantine-pick` | Embeddable Pikchr(https://pikchr.org) diagrams renderer for Obsidian(https://obsidian.md). |
| [Adapt to Current View](https://github.com/churnish/adapt-to-current-view) | `adapt-to-current-view` | Set different accent colors for Reading view, Live Preview and Source. |
| [Add an ID to the front matter](https://github.com/llimllib/obsidian-guid-plugin) | `guid-front-matter` | Add a globally unique ID to every markdown document's front matter |
| [Add links to current note](https://github.com/mrjackphil/obsidian-crosslink-between-notes) | `mrj-crosslink-between-notes` | This plugin adds a command which allows to add a link to the current note at the bottom of selected notes |
| [Addional Markdown suffix (.mdx/.svx).](https://github.com/git-no/obsidian-markdown-file-suffix) | `obsidian-markdown-file-suffix` | Use additional files like .mdx / .svx as if they were markdown. |
| [Additional Icons](https://github.com/matthewturk/obsidian-additional-icons) | `additional-icons` | Adds additional iconsets to Obsidian |
| [aDHL](https://github.com/tine-schreibt/aDHL) | `another-dynamic-highlights` | Create pretty static highlighters from search or regEx. Group by tag and set commands for toggling. Based on Dynamic Highlights. |
| [Adjacency Matrix Exporter](https://github.com/danielegrazzini/adjacency-matrix-exporter) | `adjacency-matrix-exporter` | Create a numerical adjacency matrix of your vault in two ways: Absolute and Normalized. |
| [Adjacency Matrix Maker](https://github.com/SkepticMystic/adjacency-matrix-maker) | `adjacency-matrix-maker` | Create an interactive image of an adjacency matrix of your vault |
| [Admonition](https://github.com/javalent/admonitions) | `obsidian-admonition` | Enhanced callouts for Obsidian.md |
| [Advanced Canvas](https://github.com/Developer-Mike/obsidian-advanced-canvas) | `advanced-canvas` | Supercharge your canvas experience! Create presentations, flowcharts and more! |
| [Advanced Codeblock](https://github.com/lijyze/obsidian-advanced-codeblock) | `obsidian-advanced-codeblock` | Give additioinal features to  code blocks. |
| [Advanced Copy](https://github.com/leschuster/obsidian-advanced-copy) | `advanced-copy` | Copy Markdown and transform it into HTML, Anki, or any custom format. Create custom profiles with versatile templates tailored to your workflow. |
| [Advanced Cursors](https://github.com/SkepticMystic/advanced-cursors) | `advanced-cursors` | Use multiple cursors even more powerfully. |
| [Advanced Debug Mode](https://github.com/mnaoumov/obsidian-advanced-debug-mode) | `advanced-debug-mode` | Enhances debugging experience. |
| [Advanced Merger](https://github.com/antoKeinanen/obsidian-advanced-merger) | `advanced-merger` | Merge a folder of notes for easier export. |
| [Advanced new file](https://github.com/vanadium23/obsidian-advanced-new-file) | `obsidian-advanced-new-file` | This is a plugin for choosing folder on note creation. |
| [Advanced Note Composer](https://github.com/mnaoumov/obsidian-advanced-note-composer) | `advanced-note-composer` | Enhances Note composer core plugin. |
| [Advanced Progress Bars](https://github.com/cactuzhead/Advanced-Progress-Bars) | `advanced-progress-bars` | Progress bars that can change color depending on completion value - fully customizable. |
| [Advanced Random Note](https://github.com/karstenpedersen/obsidian-advanced-random-note) | `advanced-random-note` | Open random notes with custom queries in languages like Dataview and Regex. |
| [Advanced Ruby](https://github.com/peter-yanase/obsidian-advanced-ruby) | `advanced-ruby` | Enable complex, language-independent ruby annotation rendering. |
| [Advanced Slides](https://github.com/MSzturc/obsidian-advanced-slides) | `obsidian-advanced-slides` | Create markdown-based presentations in Obsidian |
| [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) | `table-editor-obsidian` | Improved table navigation, formatting, manipulation, and formulas |
| [Advanced URI](https://github.com/Vinzent03/obsidian-advanced-uri) | `obsidian-advanced-uri` | Advanced modes for Obsidian URI |
| [Advanced Сanvas Filter](https://github.com/CHex0K/advanced-canvas-filter) | `advanced-canvas-filter` | Filter Canvas to show only items with specified tags. |
| [Age Encrypt](https://github.com/Mr-1311/obsidian-age-encrypt) | `age-encrypt` | Secure content encryption using age encryption library |
| [Aggregator](https://github.com/Seraphli/obsidian-aggregator) | `obsidian-aggregator` | This plugin helps you gather information from files, and make a summary in the file. |
| [Agile Task Notes](https://github.com/BoxThatBeat/obsidian-agile-task-notes) | `obsidian-agile-task-notes` | Import your tasks from your TFS (Azure or Jira) to take notes on them and make todo-lists! |
| [AI Agent](https://github.com/TheManuelML/obsidian-agent) | `ai-agent` | Empower your vault with Google Gemini. This AI agent integrates Google's artificial intelligence language models to help you perform tasks and conduct web searches. |
| [AI Assistant](https://github.com/qgrail/obsidian-ai-assistant) | `ai-assistant` | AI Assistant plugin for Obsidian |
| [AI bot](https://github.com/kuzzh/obsidian-ai-bot) | `ai-bot` | Polish, summarize, translate, analyze, and interpret code using AI. |
| [AI Chat](https://github.com/arenasys/obsidian-ai-chat) | `arenasys-ai-chat` | Chat with AI about your notes. |
| [AI Chat as Markdown](https://github.com/cpbotha/obsidian-ai-chat-as-md) | `ai-chat-as-md` | Multiple branching AI conversations as Markdown hierarchy |
| [AI Commander](https://github.com/yzh503/obsidian-aicommander-plugin) | `ai-commander` | Generate audio transcripts, images, and text in context of PDF attachments or web search results using OpenAI (ChatGPT) and Bing API. |
| [AI Companion](https://github.com/kowshik24/obsidian-ai-assistant) | `ai-companion` | AI companion accessible with /ai command in notes. Supports OpenAI integration. |
| [AI Editor](https://github.com/buszk/obsidian-ai-editor) | `ai-editor` | Empower your note editor with LLM capabilities. Customizable to work for your use cases. |
| [AI for Templater](https://github.com/TfTHacker/obsidian-ai-templater) | `ai-templater` | AI Extension for the Templater plugin with the OpenAI Client Library. |
| [AI Helper](https://github.com/davidjconnolly/obsidian-ai-helper) | `ai-helper` | An AI helper tool for summarizing text and providing a chatbot to let you ask questions about your notes. |
| [AI image analyzer](https://github.com/Swaggeroo/obsidian-ai-image-analyzer) | `ai-image-analyzer` | Analyze images with AI to get keywords of the image. |
| [AI Image OCR](https://github.com/rootiest/obsidian-ai-image-ocr) | `ai-image-ocr` | Extract text from handwritten notes and images using powerful AI Vision models |
| [AI integration Hub](https://github.com/hish-math/obsidian-ai-hub) | `ai-hub` | Integrate with AI models (currently Google's Gemini only) to quickly generate and refine notes. |
| [AI LaTeX Generator](https://github.com/aaaaayushh/ai-latex-generator) | `ai-latex-generator` | Convert natural language to LaTeX equations using a local LLM. |
| [AI LLM](https://github.com/Sparky4567/obsidian_ai_plugin) | `ai_llm` | Integrate local machine learning (OLLAMA) functionality into your notes, enhancing their capabilities |
| [AI Mentor](https://github.com/clementpoiret/ai-mentor) | `ai-mentor` | Meet your open source AI mentor in Obsidian. Ask questions, get answers, and learn new things. |
| [AI Note Tagger](https://github.com/jaspermayone/obsidian-ai-tagger) | `ai-note-tagger` | Automatically tag your notes using AI and update frontmatter with generated tags. |
| [AI Notes Summary](https://github.com/irbull/obsidian-ai-summary) | `ai-summary` | Summarize referenced notes using OpenAI. |
| [AI Providers](https://github.com/pfrankov/obsidian-ai-providers) | `ai-providers` | A hub for setting AI providers (OpenAI-like, Ollama and more) in one place. |
| [AI Research Assistant](https://github.com/InterwebAlchemy/obsidian-ai-research-assistant) | `ai-research-assistant` | A Prompt Engineering research utility for generative AI models like OpenAI's ChatGPT that facilitates archiving and searching conversations and live editing a conversation's context/memory. |
| [AI Revisionist](https://github.com/ProfSynapse/obsidian-revisionist) | `revisionist` | AI-powered text revision for your notes. |
| [AI Summarize](https://github.com/ravenwits/obsidian-ai-summarize) | `ai-summarize` | Summarize your notes using AI |
| [AI Tagger](https://github.com/lucagrippa/obsidian-ai-tagger) | `ai-tagger` | Analyze and tag your document with one click for efficient note organization using AI. |
| [AI Tagger Universe](https://github.com/niehu2018/obsidian-ai-tagger-universe) | `ai-tagger-universe` | Automatically analyze note content and add relevant tags using AI (with Chinese interface support) |
| [AI Tools](https://github.com/solderneer/obsidian-ai-tools) | `ai-tools` | Adding powerful semantic search, generative answers, and other AI tools to Obsidian, using Supabase + OpenAI. |
| [AI Transcriber](https://github.com/mssoftjp/obsidian-ai-transcriber) | `ai-transcriber` | AI-powered speech-to-text transcription using OpenAI GPT-4o and Whisper APIs. |
| [AI Zhipu](https://github.com/TarsLab/obsidian-ai-zhipu) | `ai-zhipu` | Generate text using the ZhipuAI API. |
| [AI-AnkiSync](https://github.com/jannusgoe/obsidian-ankisync) | `ai-enhanced-anki-sync` | Sync AI-enhanced flashcards with Anki via AnkiConnect |
| [ai-writer](https://github.com/Donovan-Ye/obsidian-ai-writer-plugin) | `ai-writer` | Use AI to generate high-quality articles with knowledge fragments. |
| [AidenLx's Folder Note - folderv component](https://github.com/aidenlx/alx-folder-note-folderv) | `alx-folder-note-folderv` | Optional `folderv` Component for alx-folder-note |
| [Air Quotes](https://github.com/alangrainger/obsidian-air-quotes) | `air-quotes` | Search and insert quotes from a source text as you type. This is great for reading a physical book or eReader while taking notes on a separate laptop or phone. The plugin can also convert ePub files to Markdown notes. |
| [Alfonso Money Manager](https://github.com/smartlife-gpt/alfonso-money-manager-obsidian) | `alfonso-money-manager` | A plugin for Alfonso Money Manager to view data in obsidian |
| [Alias from heading](https://github.com/basham/obsidian-alias-from-heading) | `obsidian-alias-from-heading` | Implicitly add an alias matching the first heading in a document. |
| [Alias Management](https://github.com/WithMarcel/alias-management) | `alias-management` | Identify duplicate notes based on similar aliases and filenames. |
| [Alias Picker](https://github.com/rostunic/obsidian-alias-picker) | `alias-picker` | Pick aliases or blocks of links. |
| [Alignment Tracker](https://github.com/FioPio/ObsidianAlignmentTracker) | `alignment-tracker` | Track character alignment using a 3x3 grid. |
| [Aloud](https://github.com/adrianlyjak/obsidian-aloud-tts) | `aloud-tts` | Highlight and speak text from your notes. Converts text to speech in real-time with lifelike voices. |
| [Alpha Bullet](https://github.com/Mara-Li/obsidian-alpha-bullet) | `alpha-bullet` | Sorts bulleted lists alphabetically. |
| [Alt-Click to Copy](https://github.com/veersheth/obsidian-alt-click-to-copy) | `alt-click-to-copy` | Alt-click to copy code! |
| [Always Color Text](https://github.com/Kazi-Aidah/always-color-text) | `always-color-text` | Automatically Colors & Highlights Text across the Vault. |
| [Amazing Marvin](https://github.com/ikuyarihS/obsidian-amazingmarvin-plugin) | `obsidian-amazingmarvin-plugin` | This is a plugin for Obsidian (https://obsidian.md) for Amazing Marvin (https://app.amazingmarvin.com/) |
| [Amazing Marvin Integration](https://github.com/open-horizon-labs/obsidian-am) | `cloudatlas-o-am` | Integration with Amazing Marvin |
| [AmpliFlow Page Publisher](https://github.com/pbjorklund/obsidian-ampliflow-page) | `ampliflow-page` | Publish notes easily to AmpliFlow (https://www.ampliflow.se) |
| [Anchor Link Display Text](https://github.com/rca-umb/anchor-link-display-text) | `anchor-display-text` | Automatically uses the linked heading as the display text for anchor links. |
| [Animated Cursor](https://github.com/kotaindah55/animated-cursor) | `animated-cursor` | Simple yet smooth animated cursor. |
| [Anki Helper](https://github.com/panAtGitHub/anki-helper) | `anki-helper` | Standardizes Anki card display for seamless integration with the expand_to_anki plugin. |
| [Anki Integration](https://github.com/NoahBoos/obsidian-anki-integration) | `anki-integration` | Create flashcards from your notes with a seamless interface, structuring them with metadata and syncing effortlessly via AnkiConnect. |
| [AnkiBridge](https://github.com/JeppeKlitgaard/ObsidianAnkiBridge) | `obsidian-ankibridge` | Yet Another Anki Bridge |
| [AnkiSync+](https://github.com/RochaG07/anki-sync-plus) | `anki-sync-plus` | Integration between Obsidian and Anki. |
| [Annotate Audio](https://github.com/12-VidE/annotate-audio) | `annotate-audio` | Listen to an audio and add comments to it. |
| [Annotator](https://github.com/elias-sundqvist/obsidian-annotator) | `obsidian-annotator` | This is a sample plugin for Obsidian. It allows you to open and annotate PDF and EPUB files. |
| [Another name](https://github.com/EurFelux/obsidian-another-name-plugin) | `another-name` | Add a another name for your file! |
| [Another Quick Switcher](https://github.com/tadashi-aikawa/obsidian-another-quick-switcher) | `obsidian-another-quick-switcher` | This is an Obsidian plugin which is another choice of Quick switcher. |
| [Another Simple Todoist Sync](https://github.com/eudennis/ultimate-todoist-sync-for-obsidian-experiment) | `another-simple-todoist-sync` | Sync tasks with Todoist from within your notes. |
| [Another Sticky Headings](https://github.com/zhouhua/obsidian-sticky-headings) | `another-sticky-headings` | Display headings tree during editing and preview to indicate the current position. |
| [Antidote Grammar Checker Integration](https://github.com/Heziode/obsidian-antidote) | `antidote-grammar-checker-integration` | Unofficial integration of Antidote, a powerful English and French grammar checker |
| [AnyBlock](https://github.com/any-block/any-block) | `any-block` | You can flexibility to create a 'Block' by some means. It also provides some useful features, like `list to table`. |
| [AnySocket Sync](https://github.com/lynxaegon/obsidian-anysocket-sync) | `anysocket-sync` | Self-Hosted synchronization for you Vault using AnySocket |
| [Aosr](https://github.com/linanwx/aosr) | `aosr` | Another obsidian spaced repetition |
| [API Designer](https://github.com/ruveydayilmaz/obsidian-api-designer-plugin) | `api-designer` | Design and document API endpoints visually without leaving your notes. |
| [APIRequest](https://github.com/Rooyca/obsidian-api-request) | `api-request` | Integrate API data into your notes with request caching, variable support, and precise JSON extraction. |
| [APL render](https://github.com/vzsky/apl-obsidian) | `apl-render` | render APL syntax |
| [Apple Books - Import Highlights](https://github.com/bandantonio/obsidian-apple-books-highlights-plugin) | `apple-books-import-highlights` | Import your Apple Books highlights and notes to Obsidian. |
| [Apple Books Highlights](https://github.com/atfzl/obsidian-apple-books-plugin) | `apple-books-highlights` | Sync your Apple Books highlights automatically |
| [Apple Reminders](https://github.com/urishiraval/obsidian-apple-reminders-plugin) | `obsidian-apple-reminders-plugin` | Plugin to integrate Apple Reminders into Obsidian |
| [Apply Patterns](https://github.com/jglev/obsidian-apply-patterns-plugin) | `obsidian-apply-patterns` | Apply custom patterns of find-and-replace in succession to text. |
| [April's Automatic Timelines](https://github.com/April-Gras/obsidian-auto-timelines) | `aprils-automatic-timelines` | Simple timeline generator for story tellers |
| [Arcana](https://github.com/A-F-V/obsidian-arcana) | `arcana` | A collection of AI powered tools |
| [Arcane Obfuscate](https://github.com/travismlee/arcane-obfuscate) | `arcane-obfuscate` | Obfuscate text with an arcane runic effect. |
| [Archive/trash to single note](https://github.com/mwoz123/archive-to-single-note) | `archive-to-single-note` | Allows to create single file archive/trash and merge(archive) old notes with it. |
| [Archiver](https://github.com/ivan-lednev/obsidian-task-archiver) | `obsidian-task-archiver` | Move completed tasks to an archive with a date tree |
| [Archivist Importer](https://github.com/archivistai/archivist-obsidian-importer) | `archivist-importer` | Import selected vault files into Archivist campaigns. |
| [ArchWiki Reader](https://github.com/lucifayr/archwiki-obsidian) | `archwiki-reader` | Read any ArchWiki page directly in Obsidian |
| [Are.na Manager](https://github.com/javierarce/arena-manager) | `arena-manager` | Publish content from your vault to Arena and the other way around. |
| [Are.na unofficial](https://github.com/0xroko/obsidian-arena-plugin) | `arena` | Allows you to save Are.na blocks as notes. |
| [Argument Map with Argdown](https://github.com/amdecker/obsidian-argdown-plugin) | `obsidian-argdown-plugin` | Allows you to write argdown codeblocks and view the maps in Preview |
| [Arrows](https://github.com/artisticat1/arrows) | `arrows-in-md` | Draw arrows across different parts of your notes, similar to on paper |
| [Arweave Uploader](https://github.com/konfuzz/arweave-uploader-plugin) | `arweave-uploader` | Convert your notes to HTML and upload to Arweave |
| [Asana](https://github.com/mryanb/obsidian-asana) | `asana` | Create Asana tasks from highlighted text or the current line in Obsidian. |
| [ASCII Tree Generator](https://github.com/michalekmatej/obsidian.md-ascii-tree-generator) | `ascii-tree-generator` | Convert indented code blocks with hierarchy markers into formatted ASCII tree diagrams. |
| [AsciiDoc Blocks Plugin](https://github.com/juracy/obsidian-asciidoc-blocks) | `obsidian-asciidoc-blocks` | A plugin to render asciidoc blocks in Obsidian, initially asciidoc tables. |
| [Asciidoc Reader](https://github.com/Voidgrown/obsidian-asciidoc) | `asciidoc-reader` | Enables the rendering of AsciiDoc. |
| [Asciidoctor editor](https://github.com/dzruyk/obsidian-asciidoc) | `asciidoctor-editor` | View and modify asciidoc pages |
| [asciimath](https://github.com/widcardw/obsidian-asciimath) | `obsidian-asciimath` | Add asciimath support for Obsidian. |
| [Asciinema Player](https://github.com/deeplook/obsidian-asciinema-player) | `asciinema-player` | Embed local and remote Asciinema asciicast files in Markdown notes. |
| [Askify Sync](https://github.com/helloworldkr/Askify-Obsidian-Sync) | `askify-obsidian-sync` | This plugin help to sync notes from Askify (https://askify.video/) to Obsidian |
| [At People](https://github.com/backmind/obsidian-at-people) | `at-people` | Use the @ to create links to people files with smart fuzzy search, accent-insensitive matching, and backlink-based ranking. |
| [Atomizer](https://github.com/Binxly/Atomizer) | `note-atomizer` | Turn any text into insightful atomic notes. |
| [Attachment Management](https://github.com/trganda/obsidian-attachment-management) | `attachment-management` | Customize your attachment path of notes independently with variables and auto rename it on change. |
| [Attachment Manager](https://github.com/chenfeicqq/obsidian-attachment-manager) | `attachment-manager` | Attachment folder name binding note name, automatically rename, automatically delete, show/hide. 附件文件夹名称绑定笔记名、自动重命名、自动删除、显示/隐藏。 |
| [Attachment Uploader](https://github.com/zhuxining/obsidian-attachment-uploader) | `attachment-uploader` | Attachment uploader plugin, which allows you customize the upload command, customize upload file type. |
| [Attachments Cache](https://github.com/luisbs/obsidian-attachments-cache) | `attachments-cache` | Store images and other attachments on the vault |
| [Attachments MD Indexer](https://github.com/iinkov/obsidian-attachments-md-indexer) | `attachments-md-indexer` | Creates searchable metadata notes for Canvas files, PDFs, and images, enhancing graph view visibility and plugin compatibility |
| [Audio Notes](https://github.com/jjmaldonis/obsidian-audio-notes) | `obsidian-audio-notes` | Create notes for audio files based on translations generated by Open AI Whisper. |
| [Audio Player](https://github.com/noonesimg/obsidian-audio-player) | `obsidian-audio-player` | Audio player with background playback, bookmarks and wave visualiser instead of the default html5 audio |
| [AudioPen Sync](https://github.com/jonashaefele/audiopen-obsidian) | `audiopen-sync` | Sync notes from AudioPen or VoiceNotes. |
| [Augmented Canvas](https://github.com/MetaCorp/obsidian-augmented-canvas) | `augmented-canvas` | Obsidian Canvas with AI features. |
| [Aut-O-Backups](https://github.com/ryanpcmcquen/obsidian-dropbox-backups) | `obsidian-dropbox-backups` | Automated backups to Dropbox for your enjoyment. |
| [Auto Anki](https://github.com/cadrianxyz/obsidian-auto-anki) | `auto-anki` | Using GPT to automate card creation for Spaced Repetiton in Anki |
| [Auto Archive](https://github.com/shanedonburke/obsidian-auto-archive) | `auto-archive` | Automatically archive notes once they reach a certain age |
| [Auto Bullet](https://github.com/takitsuba/obsidian-auto-bullet) | `auto-bullet` | Automatically inserts bullet points when you type spaces or tabs at the beginning of a line. |
| [Auto Card Link](https://github.com/nekoshita/obsidian-auto-card-link) | `auto-card-link` | Automatically fetches metadata from a url and makes it as a card-styled link |
| [Auto Class](https://github.com/nathonius/obsidian-auto-class) | `auto-class` | Automatically apply CSS classes to the markdown view based on a note's path and tags. |
| [Auto Classifier](https://github.com/HyeonseoNam/auto-classifier) | `auto-classifier` | This plugin automatically classify tag from your notes using ChatGPT API or Jina Classifier. It analyze your note (It can be title, frontmatter, content or selected area) and automatically insert tag where you set. |
| [Auto Close Tags](https://github.com/k0src/Obsidian-Auto-Close-Tags-Plugin) | `auto-close-tags` | Auto close HTML tags. |
| [Auto Correct Capitals Misspellings](https://github.com/Ummler/obsidian-auto-correct-capitals) | `auto-correct-capitals` | Automatically correct words with the first two letters in uppercase. |
| [Auto Daily Note](https://github.com/litegral/auto-daily-note) | `auto-daily-note` | Automatically creates today's daily note. Daily note plugin must be enabled |
| [Auto Definition Link](https://github.com/nmcarp99/Obsidian-Auto-Definition-Link) | `auto-definition-link` | Automatically converts text to definition links within the current folder when you type them. |
| [Auto Embed](https://github.com/GnoxNahte/obsidian-auto-embed) | `auto-embed` | Helps to embed links using markdown instead of iframe. |
| [Auto File Organizer](https://github.com/mofukuru/auto_file_organizer) | `auto-file-organizer` | Automatically organizes files into folders based on their extensions or tags |
| [Auto Filename](https://github.com/rcsaquino/obsidian-auto-filename) | `auto-filename` | Automatically rename files on the go based on the first x characters of files. |
| [Auto Folder Collapse](https://github.com/DarioCasciato/obsidian-auto-folder-collapse) | `auto-folder-collapse` | Automatically collapses subfolders when a parent folder is collapsed |
| [Auto Folder Note Paste](https://github.com/d7sd6u/obsidian-auto-folder-note-paste) | `auto-folder-note-paste` | Automagically convert the note to a folder note when pasting or drag'n'dropping an attachment. |
| [Auto Front Matter](https://github.com/conorzhong/obsidian-auto-front-matter) | `auto-front-matter` | Auto update front matter |
| [Auto Hide](https://github.com/skelato1/obsidian-auto-hide) | `obsidian-auto-hide` | Collapse sidebars when clicking on the editor/viewer panel |
| [Auto Hide Cursor](https://github.com/jmxo/obsidian-auto-hide-cursor) | `auto-hide-cursor` | Hides the cursor when scrolling and shows it again when moving the mouse. |
| [Auto Hyperlink](https://github.com/take6/obsidian-plugin-auto-hyperlink) | `auto-hyperlink` | Insert hyperlink according to user-defined rule |
| [Auto Journal](https://github.com/Ebonsignori/obsidian-auto-journal) | `auto-journal` | Opinionated journaling automation like daily notes but with backfills for the days when Obsidian wasn't opened |
| [Auto Keyword Linker](https://github.com/danrhodes/AutoKeywordLinker) | `auto-keyword-linker` | Automatically creates backlinks for specified keywords with variations and preview mode. |
| [Auto Link Title](https://github.com/zolrath/obsidian-auto-link-title) | `obsidian-auto-link-title` | This plugin automatically fetches the titles of links from the web |
| [Auto Math](https://github.com/loglux/auto-math-for-obsidian) | `auto-math` | Auto-expands LaTeX snippets. External rules with live reload, Custom Rules Editor, and default math pack. |
| [Auto Note Importer](https://github.com/uppinote20/obsidian-auto-note-importer) | `auto-note-importer` | Automatically import notes from an external database like Airtable into your Vault. |
| [Auto Note Mover](https://github.com/farux/obsidian-auto-note-mover) | `auto-note-mover` | Auto Note Mover will automatically move the active notes to their respective folders according to the rules. |
| [Auto pair chinese symbol](https://github.com/renmu123/obsidian-auto-pair-chinese-symbol) | `obsidian-auto-pair-chinese-symbol` | Auto pair chinese symbol |
| [Auto Periodic Notes](https://github.com/jamiefdhurst/obsidian-auto-periodic-notes) | `auto-periodic-notes` | Creates new periodic notes automatically in the background and allows these to be pinned in your open tabs, requires the Periodic Notes plugin. |
| [Auto Reading Mode](https://github.com/kelvinc6/auto-reading-mode) | `auto-reading-mode` | Automatically switches previously opened Markdown pages into reading mode. |
| [Auto Replacer](https://github.com/Alecell/auto-replacer) | `auto-replacer` | Replace text in your notes automatically using regex rules and JavaScript functions. Apply custom formatting, corrections, or dynamic replacements as you type. |
| [Auto Split](https://github.com/jsartelle/obsidian-auto-split) | `obsidian-auto-split` | Open notes with side-by-side editor & preview |
| [Auto Strikethrough Tasks](https://github.com/Nomekuma/auto-strikethrough-task-obsidian-pluggin) | `auto-strikethrough-task` | Automatically adds strikethrough to completed tasks. |
| [Auto switch themes between dark/light mode](https://github.com/carlrobert/double-switch) | `double-switch` | Toggling dark/light mode switches themes automatically |
| [Auto Tag](https://github.com/CtrlAltFocus/obsidian-plugin-auto-tag) | `auto-tag` | Easily generate relevant tags for your Obsidian notes or selected text. |
| [Auto Tasks](https://github.com/jamiefdhurst/obsidian-auto-tasks) | `auto-tasks` | Combine periodic notes with tags and tasks to automatically manage your daily, weekly and project TODO lists. Requires the Periodic Notes and Tasks plugins. |
| [Auto Template Trigger](https://github.com/numeroflip/obsidian-auto-template-trigger) | `auto-template-trigger` | Automatically apply or prompt for a template when creating a note. Supports assigning templates to folders. |
| [Auto-\displaystyle Inline Math](https://github.com/RyotaUshio/obsidian-auto-displaystyle-inline-math) | `auto-displaystyle-inline-math` | Automatically make all inline maths \displaystyle. |
| [Autocomplete](https://github.com/yeboster/autocomplete-obsidian) | `obsidian-autocomplete-plugin` | This plugin provides a text autocomplete feature to enhance typing speed. |
| [Autocorrect Formatter](https://github.com/b-yp/obsidian-autocorrect) | `autocorrect-formatter` | Format MarkDown content using Autocorrect. |
| [Autofit Tabs](https://github.com/bwya77/autofit-tabs) | `autofit-tabs` | Automatically adjusts tab header widths in real-time to perfectly fit each tab's title content while maintaining a clean, seamless interface that prevents awkward text truncation and ensures optimal readability of your document titles. |
| [Autogen](https://github.com/AidanTilgner/AutogenObsidianPlugin) | `autogen` | In place autogeneration of content based on prompts. |
| [autoLiterature](https://github.com/hucorz/obsidian-autoLiterature) | `auto-literature` | Assist you in taking notes for your literature. |
| [Automatic Linker](https://github.com/kdnk/obsidian-automatic-linker) | `automatic-linker` | Automatically converts plain text file references into wiki links (i.e. `[[...]]`) |
| [Automatic List Management](https://github.com/OmriLeviGit/Auto-List-Management-Obsidian) | `automatic-renumbering` | Automatically reorders checklists and numbered lists as you edit them. |
| [Automatic List Styles](https://github.com/WiseGuru/obsidian-automatic-list-styles) | `automatic-list-styles` | Automatically formats the styles of ordered lists, incrementing the list style for each layer |
| [Automatic Table Of Contents](https://github.com/johansatge/obsidian-automatic-table-of-contents) | `automatic-table-of-contents` | Create a table of contents in a note, that updates itself when the note changes |
| [Automatic Tags](https://github.com/Jamalam360/obsidian-automatic-tags) | `automatic-tags` | Add tags to new notes automatically based on their path. |
| [Automatically reveal active file](https://github.com/shichongrui/obsidian-reveal-active-file) | `obsidian-reveal-active-file` | This plugin will reveal the active file in the navigation when a file is opened. |
| [Automation](https://github.com/Benature/obsidian-automation) | `automation` | Execute commands on specific events. |
| [AutoMOC](https://github.com/dalcantara7/obsidian-auto-moc) | `auto-moc` | Looks for missing linked mentions or notes with a specific tag or alias and imports them into the current note. |
| [AutoMover](https://github.com/al0cam/AutoMover) | `auto-mover` | Move files and notes with specified names into their designated folders according to rules you define. |
| [AutoPause](https://github.com/ckep1/obsidian-autopause) | `auto-pause` | Allows one audio track to be played at a time, pausing or stopping any others. |
| [Autoplay & Loop](https://github.com/Wapply/obsidian-autoplay-and-loop) | `autoplay-and-loop` | Auto reproduces videos/audio inside notes. |
| [Autoscroll](https://github.com/petr-nazarov/obsidian-autoscroll) | `obsidian-autoscroll` | Automatically scroll content with the provided speed |
| [Avatar](https://github.com/maradotwebp/obsidian-avatar) | `avatar` | Display an avatar image in your notes. |
| [Awesome Flashcard](https://github.com/AwesomeDog/obsidian-awesome-flashcard) | `obsidian-awesome-flashcard` | Handy Anki integration for Obsidian. |
| [Awesome Image](https://github.com/AwesomeDog/obsidian-awesome-image) | `awesome-image` | One-stop solution for image management. |
| [Awesome Reader](https://github.com/AwesomeDog/obsidian-awesome-reader) | `awesome-reader` | Make Obsidian a proper Reader. |
| [AWS DynamoDb For Obsidian](https://github.com/leenattress/obsidian-plugin-dynamodb) | `obsidian-plugin-dynamodb` | Query AWS DynamoDb and render tables inside documents. |
| [Ayanite](https://github.com/jemstelos/obsidian-ayanite) | `ayanite` | Advanced AI chat interface and knowledge copilot for professionals. Turn Obsidian into an Integrated Knowledge Environment. Supports Ollama and cloud GPT providers. (Closed source) |
| [Azure DevOps Linker](https://github.com/srz2/obsidian-azure-devops-linker) | `azure-linker` | Quickly format a Azure issue tag as a link to you Azure instance. |
| [Babashka](https://github.com/filipesilva/obsidian-babashka) | `babashka` | Evaluate Clojure(Script) codeblocks in Babashka. |
| [Background Image](https://github.com/shmolf/obsidian-editor-background) | `background-image` | This allows you to specify a remote URL as the background image, and a few settings to tweak the experience. |
| [Backgroundset](https://github.com/Youngmoss/obsidian-backgroundset) | `backgroundset` | Allow you to set background image set(folder) |
| [BackItUp](https://github.com/hammadxp/back-it-up) | `back-it-up` | Quickly make a copy or snapshot of a note in Obsidian. |
| [Backlink Cache](https://github.com/mnaoumov/obsidian-backlink-cache) | `backlink-cache` | Stores backlink cache to speed up `app.metadataCache.getBacklinksForFile` |
| [Backlink Full Path](https://github.com/mnaoumov/obsidian-backlink-full-path) | `backlink-full-path` | Shows the backlink's full path in the backlinks panel. |
| [Backlink Settings](https://github.com/calvinwyoung/obsidian-backlink-settings) | `backlink-settings` | Allow saving default settings for the backlinks / "Linked mentions" pane at the bottom of notes. |
| [Backtick text selector](https://github.com/cool-RR/backtick-text-selector) | `backtick-text-selector` | Select text between backticks with keyboard shortcuts. |
| [Badges](https://github.com/gapmiss/badges) | `badges` | Add inline badges/callouts to notes. |
| [Banners](https://github.com/noatpad/obsidian-banners) | `obsidian-banners` | Add banner images to your notes! |
| [Banners Reloaded](https://github.com/dgcreations00/obsidian-banners-reloaded) | `banners-reloaded` | A simple, fast, and lightweight way to add customizable banners to your notes. |
| [Banyan](https://github.com/ratiger/obsidian-banyan) | `banyan` | A card-based homepage to browse, organize, and navigate notes effortlessly with multi-tag filtering. |
| [Barcode Generator](https://github.com/noxonad/obsidian-barcode-generator) | `barcode-generator` | Generates customizable barcodes into your notes. |
| [Base Tag Renderer](https://github.com/darrenkuro/obsidian-basetag) | `obsidian-basetag` | This plugin renders the basename of tags. |
| [Battery Indicator](https://github.com/Opisek/obsidian-battery-indicator) | `battery-indicator` | Displays current battery level in the status bar. |
| [BattleSnake Board Viewer](https://github.com/EnderInvader/battlesnake-viewer) | `battlesnake-viewer` | Render BattleSnake positions diagrams in note preview. |
| [BBCode Convertor](https://github.com/salockhart/obsidian-bbcode) | `obsidian-bbcode` | Convert Markdown files to BBCode |
| [Bearings](https://github.com/jeetsukumaran/obsidian-bearings) | `bearings` | Dynamically-scoped expanding tree views of your vault's semantic and logical architectures. |
| [Beautiful Contact Cards](https://github.com/seth10/beautiful-obsidian-contacts) | `beautiful-contact-cards` | Renders "contact" code blocks with tappable links for phone, social media, etc. |
| [Beautitab](https://github.com/andrewmcgivery/obsidian-beautitab) | `beautitab` | Creates a customizable new tab view with beautiful backgrounds, quotes, search, and more. |
| [Beeminder Word Count Plugin](https://github.com/kenzan100/beeminder-obsidian-word-count) | `beeminder-word-count-plugin` | This lets you post word counts directly from obsidian file to Beeminder. |
| [Bellboy](https://github.com/shakedlokits/obsidian-bellboy) | `obsidian-bellboy` | Opinionated file structure manager. |
| [BetaX NAS Sync](https://github.com/skye-z/ons) | `ons` | Keep Vault synchronized with the NAS on your home intranet. |
| [Better Canvas Lock](https://github.com/Mara-Li/obsidian-better-canvas-lock) | `better-canvas-lock` | Enhance the read-only mode in canvas with fully lock the scroll, zoom, drag-and-drop in read-only! |
| [Better Command Palette](https://github.com/AlexBieg/obsidian-better-command-palette) | `obsidian-better-command-palette` | A command palette that does all of the things you want it to do. |
| [Better Comment Toggle](https://github.com/MrGVSV/obsidian-better-comment-toggle) | `better-comment-toggle` | Improved comment toggling. |
| [Better Export PDF](https://github.com/l1xnan/obsidian-better-export-pdf) | `better-export-pdf` | Export your notes to PDF, support export preview, add bookmarks outline and header/footer. |
| [Better File Link](https://github.com/marcjulianschwarz/obsidian-file-link) | `obsidian-file-link` | A plugin to add better external file links to notes. |
| [Better Heading Hierarchy](https://github.com/rogerfan48/better-heading-hierarchy) | `better-heading-hierarchy` | Add guide lines to make the hierarchy of Markdown headings more visually clear. |
| [Better Inline Fields](https://github.com/dsarman/better-inline-fields) | `better-inline-fields` | Obsidian plugin to enhance Dataview style inline fields |
| [Better Link Clicker](https://github.com/eniverz/obsidian-better-link-clicker-plugin) | `better-link-clicker` | Changes link click behavior to edit on click and navigate on Ctrl+Click. |
| [Better Markdown Links](https://github.com/mnaoumov/obsidian-better-markdown-links) | `better-markdown-links` | Adds support for angle bracket links and manages relative links properly |
| [Better Math in Callouts & Blockquotes](https://github.com/RyotaUshio/obsidian-math-in-callout) | `math-in-callout` | Add better Live Preview support for math rendering inside callouts & blockquotes. |
| [Better MathJax](https://github.com/greasycat/BetterMathjax) | `better-mathjax` | Provide math autocompletion and customizable snippets. |
| [Better Mind Map](https://github.com/linem-davton/obsidian-better-mindmap) | `better-mindmap` | Visualize notes as interactive mind maps |
| [Better Order List](https://github.com/Quorafind/Obsidian-Better-Order-List) | `better-order-list` | Support new line order list like 1、 or (1)., etc. |
| [Better PDF Plugin](https://github.com/MSzturc/obsidian-better-pdf-plugin) | `better-pdf-plugin` | Goal of this Plugin in to implement a native PDF handling workflow |
| [Better Plugins Manager](https://github.com/eondrcode/obsidian-manager) | `better-plugins-manager` | Plugin Manager: Simplify, Enhance, Personalize \| 插件管理器：简化操作、增强功能、个性化设置 |
| [Better Recall](https://github.com/FlorianWoelki/obsidian-better-recall) | `better-recall` | Add anki-like spaced repetition and recall to your vault. |
| [Better Search Views](https://github.com/ivan-lednev/better-search-views) | `better-search-views` | Outliner-like breadcrumb trees for search, backlinks and embedded queries |
| [Better Word Count](https://github.com/lukeleppan/better-word-count) | `better-word-count` | Counts the words of selected text in the editor. |
| [BibDesk Integration](https://github.com/alberti42/obsidian-bibdesk-integration) | `bibdesk-integration` | Import BibTex citations into your notes and open PDF documents linked in a BibDesk library. |
| [Bible Linker](https://github.com/kuchejak/obsidian-bible-linker-plugin) | `obsidian-bible-linker` | Link multiple bible verses easily |
| [Bible linker Pro](https://github.com/Floydv149/bibleLinkerPro) | `bible-linker-pro` | Convert Bible texts to JW Library links. |
| [Bible Reference](https://github.com/tim-hub/obsidian-bible-reference) | `obsidian-bible-reference` | Taking Bible Study note in Obsidian.md application easily. Automatically suggesting Bible Verses as references. |
| [Bible sidecar](https://github.com/janisringli/bible-sidecar-obsidian-plugin) | `bible-sidecar` | Open the bible in your prefered translation in a splitscreen view |
| [BibLib](https://github.com/callumalpass/obsidian-biblib) | `biblib` | Create literature notes and manage bibliographic references. |
| [Bibtex Entry View](https://github.com/awfrok/obsidian-plugin-bibtex-entry-view) | `bibtex-entry-view` | Load the bibtex entry of a given bibkey from a given bib file and show the entry in the code block of bibkey. |
| [BibTeX Manager](https://github.com/akopdev/obsidian-bibtex-manager) | `bibtex-manager` | Create a literature notes from a BibTeX entries. |
| [BibTeX Scholar](https://github.com/liu-qilong/bibtex-scholar) | `bibtex-scholar` | A complete BibTeX citation management solution designed for contextual, frictionless literature reviews and paper writing--right inside your notes. |
| [Big Calendar](https://github.com/Quorafind/Obsidian-Big-Calendar) | `big-calendar` | Supports drag and drop, resizing, and more for events in Obsidian |
| [Binary File Manager](https://github.com/qawatake/obsidian-binary-file-manager-plugin) | `obsidian-binary-file-manager-plugin` | Detects new binary files in the vault and create markdown files with metadata. |
| [Birthday-Tracker](https://github.com/Raboro/Obsidian-Birthday-Tracker-Plugin) | `birthday-tracker` | Keep track of all birthdays of your family and friends. |
| [Bitcoin Block Stamp](https://github.com/sfr0xyz/obsidian-bitcoin-block-stamp) | `bitcoin-block-stamp` | Stamp your notes with the current Bitcoin block. |
| [BlazeJump](https://github.com/henryco/BlazeJump-Obsidian) | `blaze-jump` | Navigate through text at blazing speed. |
| [BlindFold](https://github.com/vzsky/blindfold-obsidian) | `blindfold-obsidian` | Fold text by making it completely hidden. |
| [Block Link Plus](https://github.com/Jasper-1024/block-link-plus) | `block-link-plus` | Logseq-like outliner for scoped files, block link commands, blp-view query rendering, and inline edit for embeds. |
| [Blockier](https://github.com/blorbb/obsidian-blockier) | `blockier` | Extra block editing utilities. |
| [Blockquote Levels](https://github.com/czottmann/obsidian-blockquote-levels) | `blockquote-levels` | Adds commands for increasing/decreasing the blockquote level of the current line or selection. |
| [Blockreffer](https://github.com/tyler-dot-earth/obsidian-blockreffer) | `blockreffer` | Search and embed blocks with ^block-references (aka ^block-ids) |
| [Blog AI Generator](https://github.com/garethng/obsidian-blog-generator) | `ai-blog-generator` | Generate blog posts from your notes using OpenAI API |
| [Blue Star](https://github.com/Lio5n/blue-star) | `blue-star` | Generate Anki flashcards in multiple ways. |
| [Blueprint](https://github.com/madx/blueprint-obsidian-plugin) | `blueprint` | Write once, update everywhere - note templates that pull from Properties. |
| [Blueprint Renderer](https://github.com/goderyu/obsidian-blueprint-renderer) | `blueprint-renderer` | Render Unreal Engine Blueprint nodes as interactive visual diagrams using BlueprintUE rendering engine |
| [Bluesky](https://github.com/eharris128/obsidian-bluesky) | `bluesky` | Post to Bluesky. |
| [Blur](https://github.com/gapmiss/blur) | `blur` | Create obfuscated blocks of text. |
| [Blur Mode](https://github.com/dangehub/obsidian-blur-mode) | `aqu-blur-mode` | Blur anything you want to keep your privacy. |
| [BMO Chatbot](https://github.com/longy2k/obsidian-bmo-chatbot) | `bmo-chatbot` | Generate and brainstorm ideas while creating your notes using Large Language Models (LLMs) from Ollama, LM Studio, Anthropic, Google Gemini, Mistral AI, OpenAI, and more for Obsidian. |
| [Boardgame Search](https://github.com/Marlon154/boardgame-search) | `boardgame-search` | Helps board game enthusiasts track their game collection seamlessly within their notes. |
| [Book Clipper](https://github.com/fardm/obsidian-book-clipper) | `book-clipper` | Save book details from websites into your notes. |
| [Book Search](https://github.com/anpigon/obsidian-book-search-plugin) | `obsidian-book-search-plugin` | Helps you find books and create notes. |
| [Book Smith](https://github.com/Yeban8090/book-smith) | `book-smith` | Simplify long-form writing and book creation. Organize chapters, track progress, and export your manuscript in various formats for a seamless publishing workflow. |
| [BookFusion](https://github.com/BookFusion/obsidian-plugin) | `bookfusion` | Import your BookFusion highlights & annotations into your vault. |
| [Bookmarks Caller](https://github.com/namikaze-40p/obsidian-bookmarks-caller) | `bookmarks-caller` | Easily open bookmarks. |
| [BookNav](https://github.com/jemberton/obsidian-booknav-plugin) | `booknav` | Adds a codeblock language to parse internal links and render them in a book style navigation. |
| [Bookshelf](https://github.com/weph/obsidian-bookshelf) | `bookshelf` | Organize your book notes, track your reading progress, and gain insights into your reading habits with detailed charts and statistics. |
| [Booksidian](https://github.com/MichaBrugger/booksidian_plugin) | `booksidian-plugin` | Connect Obsidian to your Goodreads. |
| [BookXNote Sync](https://github.com/CodeListening/obsidian-bookxnote) | `bookxnote-sync` | 同步bookxnote中的笔记到Obsidian中 |
| [Boost Link Suggestions](https://github.com/jglev/obsidian-boost-link-suggestions) | `boost-link-suggestions` | An Obsidian (https://obsidian.md) plugin offering an llternative inline link suggester that orders results by link count and manual boosts. |
| [Bottom to Top](https://github.com/lizard-heart/obsidian-bottom-to-top-text) | `bottom-to-top` | Reverses direction of text. |
| [BPMN](https://github.com/joleaf/obsidian-bpmn-plugin) | `bpmn-plugin` | This plugin enables viewing/editing/simulating BPMNs using bpmn-js. |
| [brAIn](https://github.com/lusob/obsidian-brain) | `brain` | This is a brAIn for Obsidian. This plugin implements a ChatGPT retrieval for your obsidian notes. |
| [Brain Dump Mode](https://github.com/yesjinu/brain-dump-mode) | `brain-dump-mode` | Done is better than perfect. Complete your first-messy-draft before you make it perfect. Your delete key will be DISABLED and all you can do is JUST BURN YOUR KEYBOARDS🔥 |
| [braincache](https://github.com/XSPGMike/braincache_obsidian) | `braincache` | Create flashcards from obsidian notes |
| [Brainframe](https://github.com/pedersen/obsidian-brainframe) | `brainframe` | This is a set of tools to help Obsidian manage extras (such as storing links like products and software) that it doesn't currently do. |
| [BRAT](https://github.com/TfTHacker/obsidian42-brat) | `obsidian42-brat` | Easily install a beta version of a plugin for testing. |
| [Breadcrumbs](https://github.com/SkepticMystic/breadcrumbs) | `breadcrumbs` | Add structured hierarchies to your notes |
| [Broken Links](https://github.com/ipshing/obsidian-broken-links) | `broken-links` | Find broken links in your vault that don't connect to notes. |
| [Browser History](https://github.com/noy4/browser-history) | `browser-history` | Sync your browser history to notes. |
| [Browser Interface](https://github.com/jason-lieb/obsidian-browser-interface-plugin) | `browser-interface` | Save and reopen browser tabs using your vault and a browser extension. |
| [Buckwalter Transliteration](https://github.com/amrojjeh/obsidian-buckwalter) | `buckwalter-transliteration` | Renders Arabic using Buckwalter's encoding scheme. |
| [BuJo Bullets](https://github.com/frankolson/obsidian-bujo-bullets) | `bujo-bullets` | Alternate checkbox types to support Bullet Journal bullets |
| [Bulk Exporter](https://github.com/symunona/obsidian-bulk-exporter) | `bulk-exporter` | Use Dataview queries to export a set of notes with assets |
| [Bulk open selected links](https://github.com/autohub7/obsidian-open-selected-links) | `bulkopen-selected-links` | This plugin allows users to easily open all selected links in edit mode. |
| [Bulk Rename](https://github.com/OlegLustenko/obsidian-bulk-rename) | `obsidian-bulk-rename-plugin` | Purpose of this plugin rename files based on pattern |
| [Buttondown](https://github.com/caro401/obsidian-buttondown) | `obsidian-buttondown-plugin` | Send your notes to your buttondown.email account as email drafts. |
| [Buttons](https://github.com/shabegom/buttons) | `buttons` | Create Buttons in your Obsidian notes to run commands, open links, and insert templates |
| [Byte Field Diagrams](https://github.com/natri0/obsidian-bytefield) | `bytefield` | Adds diagrams that show how structures are laid out in memory / network. |
| [CalcCraft](https://github.com/klaudyu/CalcCraft) | `calc-craft` | have formulas like in excel a1+a2, or sum() |
| [Calctex](https://github.com/Developer-Mike/obsidian-calctex) | `calctex` | Calculate LaTeX formulas inside Obsidian. |
| [Calculite](https://github.com/gfxholo/calculite) | `calculite` | Standard calculator with a simple button layout. |
| [Calendar (Beta)](https://github.com/liamcain/obsidian-calendar-plugin) | `calendar` | Calendar view of your daily notes |
| [Calendar Bases](https://github.com/edrickleong/obsidian-calendar-bases) | `calendar-bases` | Adds a calendar layout to bases so you can display notes with dates in an interactive calendar view. |
| [Calendar Event Sync](https://github.com/stephendolan/obsidian-calendar-event-sync) | `calendar-event-sync` | Sync a relevant calendar event to your current note. |
| [Calendarium](https://github.com/javalent/calendarium) | `calendarium` | Craft mind-bending fantasy and sci-fi calendars. |
| [Calibre](https://github.com/caronchen/obsidian-calibre-plugin) | `obsidian-calibre-plugin` | This plugin allows you to access your calibre libraries and read books directly in Obsidian. |
| [Callout Copy Buttons](https://github.com/alythobani/obsidian-callout-copy-buttons) | `callout-copy-buttons` | Adds copy buttons to callout blocks in your notes. |
| [Callout Integrator](https://github.com/Cleoche/obsidian-callout-integrator) | `callout-integrator` | Integrate long blocks of text into callouts and easier nested callouts |
| [Callout Manager](https://github.com/eth-p/obsidian-callout-manager) | `callout-manager` | Easily create and customize callouts. |
| [Callout menu](https://github.com/anareaty/callout-menu) | `callout-menu` | Adds some extra options to callouts context menu and allows you to add your own custom callouts. |
| [Callout Suggestions](https://github.com/cwfryer/obsidian-callout-suggestions) | `callout-suggestions` | Adds a fuzzy searched suggestion modal for callouts. |
| [Callout Toggles](https://github.com/alythobani/obsidian-callout-toggles) | `callout-toggles` | Quickly add, change, or remove callouts in your notes. |
| [CalloutX](https://github.com/br4in/calloutX) | `calloutx` | An easy way to explore, visualise, and modify callout icons. |
| [Camera](https://github.com/aldrinjenson/obsidian-camera) | `obsidian-camera` | Camera plugin for Obsidian |
| [Cannoli](https://github.com/DeabLabs/cannoli) | `cannoli` | Create and run LLM scripts on the Obsidian Canvas. |
| [Canvas Blocks](https://github.com/Kay607/obsidian-canvasblocks) | `canvasblocks` | Execute scripts from canvas |
| [Canvas Card Background Remover](https://github.com/luxmargos/obsidian-canvas-card-bg-remover) | `canvas-card-bg-remover` | You can make the background of cards transparent in the Canvas |
| [Canvas Connect](https://github.com/camadkins/obsidian-canvas-connect) | `canvas-connect` | Automatically updates Canvas connection anchors based on node position, with smart routing and visual feedback. |
| [Canvas Conversation](https://github.com/AndreBaltazar8/obsidian-canvas-conversation) | `obsidian-canvas-conversation` | Canvas Conversation is a plugin that allows you to create a ChatGPT conversation using Canvas Cards. |
| [Canvas CSS class](https://github.com/Mara-Li/obsidian-canvas-css-class) | `canvas-css-class` | Add a CSS class to the canvas, but also other attributes. |
| [Canvas Daily Note](https://github.com/andrewmcgivery/obsidian-canvas-dailynote) | `canvas-dailynote` | Allows you to add a daily note node to the canvas that will always show todays note. |
| [Canvas Explorer](https://github.com/hjamet/Canvas-Explorer) | `canvas-explorer` | Explore your Obsidian vault by adding or ignoring linked notes, generating a customizable canvas with note sorting and section exclusion. |
| [Canvas Filter](https://github.com/IKoshelev/Obsidian-Canvas-Filter) | `canvas-filter` | This plugin lets you filter Canvas to only show items of specific color, tags or only connected to currently selected node. |
| [Canvas Format Brush](https://github.com/wenlzhang/obsidian-canvas-format-brush) | `canvas-format-brush` | Copy and paste formatting attributes (size and color) between canvas elements, similar to the format painter in Word. |
| [Canvas Keyboard Pan](https://github.com/nathonius/obsidian-canvas-pan) | `canvas-keyboard-pan` | Pan around your canvas using the keyboard |
| [Canvas Link Optimizer](https://github.com/Qbject/obsidian-canvas-link-optimizer) | `canvas-link-optimizer` | Optimize canvas links by displaying a page thumbnail. |
| [Canvas Link to Group](https://github.com/TGRRRR/Canvas-link-to-group) | `canvas-link-to-group` | Create links to specific groups in Canvas and jump directly to them. |
| [Canvas Links](https://github.com/aqav/obsidian-canvas-links) | `canvas-links` | Show the "links" between Canvas and File. |
| [Canvas LLM](https://github.com/farlenkov/obsidian-canvas-llm) | `canvas-llm` | A canvas-like UI to talk with LLMs. |
| [Canvas LLM Extender](https://github.com/Phasip/obsidian-canvas-llm-extender) | `canvas-llm-extender` | Let an LLM add nodes to your canvas. |
| [Canvas Mindmap](https://github.com/Quorafind/Obsidian-Canvas-MindMap) | `canvas-mindmap` | A plugin to make your canvas work like a mindmap. |
| [Canvas Mindmap Helper](https://github.com/tim-smart/obsidian-canvas-mindmap) | `canvas-mindmap-helper` | Make the Canvas work like a mindmap |
| [Canvas minimap](https://github.com/ifree/Obsidian-canvas-minimap) | `canvas-minimap` | For easy navigation in large canvas |
| [Canvas Picture in Picture](https://github.com/h-sphere/obsidian-canvas-picture-in-picture) | `canvas-picture-in-picture` | Enables ability to pin Canvas nodes and float them above the board (Picture-in-Picture mode) |
| [Canvas Presentation](https://github.com/Quorafind/Obsidian-Canvas-Presentation) | `canvas-presentation` | A plugin to help you display cards based on sequence. |
| [Canvas Random Note](https://github.com/jmilldotdev/obsidian-canvas-randomnote) | `canvas-randomnote` | Add random notes from your vault to the Obsidian canvas |
| [Canvas Send to Back](https://github.com/Zachatoo/obsidian-canvas-send-to-back) | `canvas-send-to-back` | Send a card in Obsidian Canvas to be behind all other cards. |
| [Canvas2Document](https://github.com/slnsys/obsidian-canvas2document) | `canvas2document` | Convert a complete Canvas to a long form document, integrating all cards, notes, images and other media content into a single markdown file. |
| [CAO](https://github.com/iamgodot/CAO) | `cao` | Integrate Claude AI for chatting in notes. |
| [Capitaliser](https://github.com/eoliversec/obsidian-capitalise-plugin) | `capitaliser` | Cycle text capitalisation (lowercase, Capitalise Each Word, UPPERCASE). |
| [Card Forge](https://github.com/carlsverre/obsidian-card-forge) | `card-forge` | Convert notes into printable cards. |
| [Card View Mode](https://github.com/yo-goto/obsidian-card-view-mode) | `obsidian-card-view-mode` | Enable to view your notes as cards. |
| [Card View Switcher](https://github.com/qawatake/obsidian-card-view-switcher-plugin) | `obsidian-card-view-switcher-plugin` | Quick switcher with card view |
| [Card Viewer](https://github.com/vsme/obsidian-card-viewer) | `card-viewer` | Display cards for movies, TV shows, books, and music. |
| [CardBoard](https://github.com/roovo/obsidian-card-board) | `card-board` | Display markdown tasks on kanban style boards. |
| [Cardify](https://github.com/joshuakto/obsidian-cardify) | `cardify` | This is a plugin to cardify markdown contents into subsequent markdown files. |
| [CardNote](https://github.com/cycsd/obsidian-card-note) | `card-note` | Help you quickly extract your thoughts in the Canvas and Excalidraw |
| [Cards View](https://github.com/jillro/obsidian-cards-view-plugin) | `cards-view` | Displays a card view of your notes. |
| [Caret](https://github.com/jcollingj/caret) | `caret` | Accelerate your work with LLMs in canvas and your notes |
| [Carry-Forward](https://github.com/jglev/obsidian-carry-forward) | `obsidian-carry-forward` | An Obsidian Notes plugin for generating and copying block IDs and for copying lines with links to the copied line. |
| [Change Case](https://github.com/dbrockman/obsidian-change-case) | `change-case` | Plugin to let you change the case (UPPER CASE, camelCase, snake_case, etc) of the current selection. |
| [Character Insertion](https://github.com/TakamiChie/Obsidian_CharacterInsertionPlugin) | `character-insertion` | Plugin to insert a specified symbol under the cursor |
| [Character Sheets](https://github.com/Grayvox/obsidian-character-sheets) | `character-sheets` | Create character sheets for your very own traumatized little guys. |
| [Charts](https://github.com/phibr0/obsidian-charts) | `obsidian-charts` | This Plugin lets you create Charts within Obsidian |
| [Charts View](https://github.com/caronchen/obsidian-chartsview-plugin) | `obsidian-chartsview-plugin` | Data visualization solution in Obsidian based on Ant Design Charts. |
| [Chat clips](https://github.com/sleepingraven/obsidian-chat-clips) | `chat-clips` | Record chat in ordinary markdown list. |
| [Chat Stream](https://github.com/rpggio/obsidian-chat-stream) | `chat-stream` | Create branching GPT chats using canvas notes. |
| [Chat View](https://github.com/adifyr/obsidian-chat-view) | `obsidian-chat-view` | Chat View enables you to create elegant Chat UIs in your Obsidian markdown files. It also supports the WebVTT format. |
| [ChatCBT](https://github.com/clairefro/obsidian-chat-cbt-plugin) | `chat-cbt` | Guides you in reframing negative thoughts and keeping record of your discoveries |
| [ChatGPT Definition](https://github.com/julix14/chatGPT-Obsidian) | `chatgpt-definitions` | Let your AI assistant ChatGPT define words and concepts for you. |
| [ChatGPT MD](https://github.com/bramses/chatgpt-md) | `chatgpt-md` | A seamless integration of ChatGPT, OpenRouter.ai and local LLMs via Ollama into Obsidian. |
| [Chatty](https://github.com/SSaquif/obsidian-chatty) | `chatty` | Allows you to listen to your notes using text-to-speech. Uses the browser's built-in speech synthesis capabilities and your default system voices. |
| [Check and Delete](https://github.com/Danitiate/check-and-delete) | `check-and-delete` | Quickly clean up temporary list-items with the press of a button |
| [Checkbox 3 states](https://github.com/hrenaud/obsidian-checkbox3states-plugin) | `obsidian-checkbox3states-plugin` | This is a simple plugin for add a third state to checkbox list. |
| [Checkbox Autochecker](https://github.com/klaasklee/checkbox-autochecker-obsidian) | `checkbox-autochecker` | Automatically sync parent and child checkboxes with flexible propagation modes in Markdown Files. |
| [Checkbox Reorder](https://github.com/Erl-koenig/obsidian-checkboxReorder) | `checkbox-reorder` | Reorder completed checkboxes to the end of the according list. |
| [Checkbox Sort](https://github.com/mattang687/obsidian-checkbox-sort) | `checkbox-sort` | Automatically moves completed checkboxes to the end of the list |
| [Checkbox Sounds](https://github.com/yasd251/checkbox-sounds-plugin) | `checkbox-sounds` | Adds a nice completion sound when a checkbox is ticked-off |
| [Checkbox Style Menu](https://github.com/ReticentEclectic/checkbox-style-menu) | `checkbox-style-menu` | Provides an intuitive menu for quickly changing checkbox styles. |
| [Checkbox styling helper](https://github.com/jaewonE/checkbox-styling-helper) | `checkbox-styling-helper` | Helps you styling checkboxes in preview mode. |
| [Checkbox Sync](https://github.com/groldsf/obsidian_check_plugin) | `checkbox-sync` | Automatically checks the parent checkbox if all child checkboxes are completed, and unchecks it otherwise. |
| [Checkbox Time Tracker](https://github.com/udus122/checkbox-time-tracker) | `checkbox-time-tracker` | Insert timestamp when you check off the checkbox |
| [Checklist](https://github.com/delashum/obsidian-checklist-plugin) | `obsidian-checklist-plugin` | Combines checklists across pages into users sidebar |
| [Checklist Progress](https://github.com/acidghost/obsidian-checklist-progress) | `checklist-progress` | Automatically fill progress (as fraction or percentage) of check-lists. |
| [Checklist Reset](https://github.com/lhansford/obsidian-checklist-reset) | `obsidian-checklist-reset` | Adds a command to reset the state of any checklists in a document in Obsidian. |
| [Chem](https://github.com/Acylation/obsidian-chem) | `chem` | Providing chemistry supports. Rendering SMILES strings into chemistry structures. |
| [Chemical Structure Renderer](https://github.com/xaya1001/obsidian-Chemical-Structure-Renderer) | `chemical-structure-renderer` | Render chemical structures from SMILES strings into PNG or SVG format using Ketcher and Indigo Service. |
| [Chess Study](https://github.com/chrislicodes/obsidian-chess-study) | `chess-study` | A chess study helper and PGN viewer/editor. |
| [Chessboard Viewer](https://github.com/THeK3nger/obsidian-chessboard) | `obsidian-chessboard` | Render chess positions diagrams in a note. |
| [Chesser](https://github.com/SilentVoid13/Chesser) | `chesser-obsidian` | A chess game viewer/editor |
| [Chinese Calendar](https://github.com/DevilRoshan/obsidian-lunar-calendar) | `chinese-calendar` | 符合中国习惯的日历，可以显示农历、节日、调休、节气等信息，支持月视图和年视图切换，支持点击日期创建笔记，支持使用QuickAdd插件创建笔记。 |
| [Chinese chess](https://github.com/west-shell/obsidian-xiangqi) | `xiangqi` | A Chinese Chess (象棋/xiangqi) plugin designed for Obsidian |
| [Chord Sheets](https://github.com/olvidalo/obsidian-chord-sheets) | `chord-sheets` | Work with chord sheets (chords over lyrics) in your Vault: Chord diagrams, transpose, autoscroll and more. Works in live preview and reading mode. |
| [chord-lyrics](https://github.com/nevernotmove/obsidian-chordlyrics) | `chord-lyrics` |  |
| [Chorded Hotkeys](https://github.com/ConnorMeyers/obsidian-chorded-hotkeys) | `obsidian-chorded-hotkeys` | Type multiple letters at the same time to trigger text insertion, template insertion, or command execution. |
| [Christmas](https://github.com/Matse2005/Obsidian-Christmas) | `christmas` | Track the time left till Christmas. |
| [Chronology](https://github.com/Canna71/obsidian-chronology) | `chronology` | Provides a calendar and a timeline of the notes creation and modification |
| [Chronos Timeline](https://github.com/clairefro/obsidian-plugin-chronos) | `chronos` | Render interactive timelines in your notes from Markdown |
| [Chronotyper](https://github.com/BambusControl/obsidian-chronotyper) | `chronotyper` | Track how long you edit notes directly in the note properties |
| [Cicada Synchronizer](https://github.com/adapole/cicada-sync) | `cicada-sync` | uses Git to synchronize vaults for team collaboration. |
| [Circuit Sketcher](https://github.com/code-forge-temple/circuit-sketcher-obsidian-plugin) | `circuit-sketcher` | Draw circuits on a canvas using circuit-sketcher-core. |
| [CircuitJS](https://github.com/StevenGann/obsidian-circuitjs) | `obsidian-circuitjs` | Embed interactive CircuitJS circuit simulations in your notes with offline support |
| [Citation Callouts](https://github.com/Marvive/Citation-Callouts) | `citation-callouts` | Elegantly formats quotes with citations from various sources into custom callouts. |
| [Citations](https://github.com/hans/obsidian-citation-plugin) | `obsidian-citation-plugin` | Automatically search and insert citations from a Zotero library |
| [CJK Count](https://github.com/vrabe/obsidian-cjk-count) | `cjk-count` | A word counter that only counts Chinese, Japanese and Korean (CJK) characters. |
| [Class Relation Visualization](https://github.com/Cold-dragon7/Obsidian-Class-Relation-Visualization) | `class-relation-visualization` | Class relation expression test |
| [Clear Todos](https://github.com/gutentag2012/obsidian-plugin-clear-todos) | `clear-todos` | Quickly remove all completed todos from your notes or selected text. |
| [Clear Unused Images](https://github.com/ozntel/oz-clear-unused-images-obsidian) | `oz-clear-unused-images` | Clear the images that you are not using anymore in your markdown notes to save space. |
| [Click Clack](https://github.com/Acylation/obsidian-click-clack) | `click-clack` | Simulates typewriter / mechanical keyboard sounds. |
| [Click Hint](https://github.com/kbwo/obsidian-click-hint) | `click-hint` | Provide keyboard-driven hints for clickable elements |
| [ClickUp sync](https://github.com/hokim-m/click-up-x-obsidian) | `click-up-sync` | Manage ClickUp space from notes |
| [Clipboard Manager](https://github.com/ayu5h-raj/clipboard-manager) | `clipboard-manager` | A clipboard manager that stores clipboard history and provides search functionality with real-time updates |
| [Cliplet](https://github.com/namikaze-40p/obsidian-cliplet) | `cliplet` | A clipboard and snippet manager — your own, separate from the OS clipboard. |
| [Clipper](https://github.com/jgchristopher/obsidian-clipper) | `obsidian-clipper` | This plugin helps you capture highlights from the web. |
| [Clipper Catalog](https://github.com/soundslikeinfo/obsidian-clipper-catalog) | `clipper-catalog` | A catalog view of all the clippings gathered with a common source property. |
| [ClipperMaster](https://github.com/aqeja/ClipperMaster-for-Obsidian) | `clippermaster` | Works with the ClipperMaster Chrome extension to clip structured content from the web and save it to your vault as Markdown files. |
| [Clojure Plugin Host](https://github.com/farcaller/obsidian-clojure-plugin-host) | `clojure-plugin-host` | A clojure plugin host, allowing the creation of simple clojure-based plugins right inside the editor. |
| [Clone Vault](https://github.com/laantorchaweb/clone-vault) | `clone-vault` | Clones the current vault by copying settings and folder structure without note contents. |
| [Close Window When Empty](https://github.com/TaylorJadin/close-window-when-empty) | `close-window-when-empty` | Close the window when the last note is closed, kind of how browsers work. |
| [Cloud Atlas](https://github.com/open-horizon-labs/obsidian-client) | `cloud-atlas` | Cloud Atlas provides a unique way to use content from your vault with ChatGPT. Reference a note and it (optionally) gets resolved and sent along. We also provide a Canvas interface for ChatGPT. Advanced features include chaining results and batching. |
| [Cloud Storage](https://github.com/yingjialong/obsidian-CloudStorage) | `cloud-storage` | Managing attachments across devices. Automatically uploads your attachments to the cloud and smartly updates all your markdown links, keeping your notes and attachments perfectly organized. Whether you're handling images, PDFs, or any other files, it works seamlessly in the background. You can even use it as a powerful image hosting solution, supporting plugin-provided cloud storage or custom S3 storage! |
| [Cloud sync](https://github.com/ai-bytedance/obsidian-cloud-sync) | `cloud-sync` | 将笔记同步到多种云盘服务，提供端到端加密保护。 |
| [Cloudinary](https://github.com/uday-samsani/obsidian-cloudinary) | `cloudinary` | Make you notes lighter by uploading all content(images, videos, audio) to Cloudinary and insert(copy or drag both) them into your notes. |
| [Cloudinary Uploader](https://github.com/jordanhandy/obsidian-cloudinary-uploader) | `obsidian-cloudinary-uploader` | This plugin uploads the media files in your clipboard (or drag and drop) to Cloudinary as unsigned uploads |
| [Cloze](https://github.com/DearVikki/obsidian-cloze-plugin) | `cloze` | Convert highlights, underlines, bolded texts or any selected texts into clozes. |
| [Cluster](https://github.com/lorens-osman-dev/cluster) | `cluster` | Make the notes clustering simpler on mobile devices and work well on PCs ether, Notes Clustering is the process of creating hierarchical notes structures. |
| [CmdSearch](https://github.com/SpaceshipCaptain/CmdSearch) | `cmd-search` | Use the command pallete to search web. Add your own URLs. |
| [cMenu](https://github.com/chetachiezikeuzor/cMenu-Plugin) | `cmenu-plugin` | cMenu is a plugin that adds a minimal text editor modal for a smoother writing/editing experience ✍🏽. |
| [Coalesce](https://github.com/bfloydd/coalesce) | `coalesce` | Coalesce your notes into a single view |
| [CoCo AskAI](https://github.com/yamfeel/coco-askai) | `coco-askai` | Let your questions flow swiftly with CoCo AskAI. (Closed source) |
| [Code Block](https://github.com/paddan/code-block-plugin) | `code-block-plugin` | This plugin converts text into code blocks with automatic language detection. |
| [Code block from selection](https://github.com/dy-sh/obsidian-code-block-from-selection) | `code-block-from-selection` | Adds code block for the selected text |
| [Code Block Labels](https://github.com/stbowers/obsidian-codeblock-labels) | `obsidian-codeblock-labels` | Adds labels to fenced code blocks |
| [Code Blocks commands](https://github.com/dragonish/code-blocks-commands) | `code-blocks-commands` | Provide commands to insert code blocks with markup, and support triggering commands with backticks. |
| [Code Editor Shortcuts](https://github.com/timhor/obsidian-editor-shortcuts) | `obsidian-editor-shortcuts` | Add keyboard shortcuts (hotkeys) commonly found in code editors such as Visual Studio Code (vscode) or Sublime Text |
| [Code Emitter](https://github.com/mokeyish/obsidian-code-emitter) | `code-emitter` | An Obsidian plugin that allows code blocks to be executed interactively like in Jupyter Notebooks. Supports languages like Rust, Kotlin, Python, JavaScript, TypeScript etc. |
| [Code Files](https://github.com/lukasbach/obsidian-code-files) | `code-files` | Edit Code Files in Obsidian with VSCode's powerful Monaco Editor |
| [Code Language Completer](https://github.com/stanley-910/obsidian-code-language-completer) | `code-language-completer` | Autosuggests and completes codeblock language options based on history. |
| [Code Link](https://github.com/observerw/obsidian-code-link) | `code-link` | Link to code files in your notes |
| [Code Preview](https://github.com/hankjs/obsidian-code-preview) | `obsidian-code-preview` | Code Preview |
| [Code Styler](https://github.com/mayurankv/Obsidian-Code-Styler) | `code-styler` | Style and customize codeblocks and inline code in both editing mode and reading mode. |
| [Code::Stats](https://github.com/Miskamyasa/obsidian-codestats) | `codestats` | The Code::Stats plugin allows you to track your coding progress and earn XP for writing markdown in the Obsidian editor. |
| [Codeblock Customizer](https://github.com/mugiwara85/CodeblockCustomizer) | `codeblock-customizer` | This Obsidian plugin lets you customize your codeblocks in editing, and reading mode as well. |
| [CodeBlock Tabs](https://github.com/JeminMau/Obsidian-CodeBlock-Tabs) | `codeblock-tabs` | Create tab group for contiguous CodeBlocks. |
| [Codeblock Template](https://github.com/sylcool/obsidian-codeblock-template) | `codeblock-template` | Re-use content within codeblocks using variables. |
| [Codeless Heatmap Calendar](https://github.com/webtechaccess/obsidian-heatmap-calendar) | `codeless-heatmap-calendar` | Fully-featured activity visualizer powered by Toggl data and more. |
| [Codename](https://github.com/dstack/obsidian-codename) | `codename` | A plugin to solve the hardest problem - naming thing. |
| [CodeScript Toolkit](https://github.com/mnaoumov/obsidian-codescript-toolkit) | `fix-require-modules` | Allows to do a lot of things with JavaScript/TypeScript scripts from inside the app. |
| [Cognitive Architect Sync](https://github.com/bhavers/obsidian-ca) | `ca-sync` | Synchronise Cognitive Architect (aka IBM IT Architect Assistant) architectures. |
| [Collapse All](https://github.com/nathonius/obsidian-collapse-all) | `obsidian-collapse-all-plugin` | Extends collapse/expand all with commands that can be bound to hotkeys. |
| [Collapse Linked Mentions](https://github.com/n810K/obsidian-collapse-linked-mentions) | `collapse-linked-mentions` | Automatically collapse embedded backlink mentions |
| [Collapse Node](https://github.com/Quorafind/Obsidian-Collapse-Node) | `collapse-node` | Collapse node in canvas. |
| [Collapsible Code Blocks](https://github.com/bwya77/collapsible-code-blocks) | `collapsible-code-blocks` | Makes code blocks collapsible in reader view and edit view as well as enabling scroll-able code blocks. |
| [Color cycler](https://github.com/tjbrennan/obsidian-color-cycler) | `color-cycler` | Dynamically change the accent color of the theme. |
| [Color Folders and Files](https://github.com/Mithadon/obsidian-color-folders-files) | `color-folders-files` | Customize the appearance of folders and files in the file explorer. |
| [Color Palette](https://github.com/ALegendsTale/obsidian-color-palette) | `color-palette` | Create and insert color palettes into your notes. |
| [Colored Tags](https://github.com/pfrankov/obsidian-colored-tags) | `colored-tags` | Colorizes tags in different colors. Colors of nested tags are mixed with the root tag to improve readability. Text color contrast is automatically matched to comply with AA level of WCAG 2.1. |
| [Colored Tags Wrangler](https://github.com/code-of-chaos/obsidian-colored_tags_wrangler) | `colored-tags-wrangler` | Assign colors to tags. Has integrations with other plugins, like Kanban. |
| [Colored Text](https://github.com/erincayaz/obsidian-colored-text) | `colored-text` | Color the selected texts. |
| [Colorful Note Background](https://github.com/andresgongora/obsidian-colorful-note-background) | `colorful-note-background` | Set note background based on file location or frontmatter metadata. |
| [Colorful Note Borders](https://github.com/rusi/obsidian-colorful-note-borders) | `colorful-note-borders` | Add customizable colorful borders to notes based on folder location or frontmatter metadata, enhancing visual organization in Obsidian. |
| [Colorizelt](https://github.com/WiNE-iNEFF/colorizelt) | `colorizelt` | Easy color and clear selected text |
| [Columns](https://github.com/tnichols217/obsidian-columns) | `obsidian-columns` | Allows you to create columns in Obsidian Markdown |
| [Combo Colors](https://github.com/kevinkickback/Combo-Colors) | `combo-colors` | Automatically apply color to fighting game combo notations. |
| [Come Down](https://github.com/mntno/obsidian-come-down) | `come-down` | Maintains a cache of your notes’ embedded external images. |
| [Come Through](https://github.com/mntno/obsidian-come-through) | `come-through` | Drill flashcards using spaced repetition. |
| [Command Alias](https://github.com/yajamon/obsidian-command-alias-plugin) | `obsidian-command-alias-plugin` | This plugin gives aliases to Obsidian commands. |
| [Command Block List](https://github.com/RyotaUshio/obsidian-command-block-list) | `command-block-list` | Hide unwanted commands from the command palette. |
| [Command Line](https://github.com/sstallion/obsidian-command-line) | `command-line` | Copy command lines from your notes to the clipboard. |
| [Command Palette--](https://github.com/qawatake/obsidian-command-palette-minus-plugin) | `obsidian-command-palette-minus-plugin` | Command palette without unwanted commands |
| [Command Tracker](https://github.com/namikaze-40p/obsidian-command-tracker) | `command-tracker` | Track the number of times the command is used. |
| [Commander](https://github.com/phibr0/obsidian-commander) | `cmdr` | Customize your workspace by adding commands everywhere, create Macros and supercharge your mobile toolbar. |
| [Commando](https://github.com/qaptoR/Commando) | `commando-command-repeater` | Enables the user to provide the number of times to repeat a command. |
| [Comments](https://github.com/JasperSurmont/obsidian-comments) | `comments` | Add comments to your markdown files to facilitate collaboration. |
| [Companion](https://github.com/rizerphe/obsidian-companion) | `companion` | Autocomplete with AI, including ChatGPT and ollama, through a copilot-like interface. |
| [Completed Area](https://github.com/DahaWong/obsidian-completed-area) | `completed-area` | Move completed to-do items to a seperate completed area. |
| [Completed Task Display](https://github.com/heliostatic/completed-task-display) | `completed-task-display` | Provides a button in the ribbon to hide or display completed tasks |
| [Completed Tasks](https://github.com/mgussekloo/obsidian-completedtasks) | `completed-tasks` | Automatically sort completed tasks to the bottom of the list. |
| [Completr](https://github.com/tth05/obsidian-completr) | `obsidian-completr` | This plugin provides advanced auto-completion functionality for LaTeX, Frontmatter and standard writing. |
| [Conditional Properties](https://github.com/diegoeis/obsidian-conditional-properties) | `conditional-properties` | Automate your frontmatter with smart IF/THEN rules. Set properties, modify titles, and keep your vault organized—automatically. |
| [Confluence Converter](https://github.com/addozhang/obsidian-confluence-converter) | `confluence-converter` | Convert markdown to Confluence wiki markup. |
| [Confluence Import](https://github.com/KkEi34/confluence-to-obsidian-plugin) | `confluence-to-obsidian` | Import Confluence space into Obsidian vault |
| [Confluence Integration](https://github.com/markdown-confluence/obsidian-integration) | `confluence-integration` | This plugin allows you to publish your notes to Confluence |
| [Confluence Link](https://github.com/BungaRazvan/confluence-link) | `confluence-link` | Upload files to confluence pages |
| [Confluence Sync](https://github.com/kerry/obsidian-confluence-sync) | `confluence-sync` | Sync Obsidian notes with Confluence |
| [Connections](https://github.com/evancleve/obsidian-connections) | `connections` | Define and view named connections between your notes. |
| [Consecutive Lists](https://github.com/jtucker2/obsidian-consecutive-lists) | `consecutive-lists` | Create consecutive lists that are displayed separately in reading mode. |
| [Consistent Attachments and Links](https://github.com/dy-sh/obsidian-consistent-attachments-and-links) | `consistent-attachments-and-links` | This plugin ensures the consistency of attachments and links |
| [Console Markdown](https://github.com/dellermann/obsidian-console) | `console` | Renders console commands and their output. |
| [Contact Cards](https://github.com/aegixx/obsidian-contact-cards) | `contact-cards` | Transforms raw data into a beautifully designed contact card for People and Organizations. |
| [Contacts](https://github.com/vbeskrovnov/obsidian-contacts) | `obsidian-contacts` | Allows you to manage and organize your contacts. |
| [Content Cards](https://github.com/liqms/obsidian-content-cards) | `content-cards` | Insert content cards in Markdown, such as timeline, highlightblock, target card, book information card, music information card, movie information card, photoes ablum, business card, content subfield, countdown, SWOT, BCG. |
| [Content Linker](https://github.com/Medill-East/obsidian-content-linker) | `content-linker` | A plugin for searching and adding bi-directional links to existing content in Obsidian Vault. |
| [Content OS](https://github.com/eharris128/obsidian-content-os) | `content-os` | Post directly to LinkedIn from your vault. |
| [Content-Addressed Attachments](https://github.com/NateScarlet/obsidian-content-addressed-attachments) | `content-addressed-attachments` | Stores attachments using content-based addressing (similar to IPFS) for automatic deduplication, but can operates entirely locally without requiring the IPFS network. Also supports github private repository for hosting. |
| [Contentful Publisher](https://github.com/ziyafenn/obsidian-contentful-publisher) | `contentful-publisher` | Manage your Contentful content from Obsidian. |
| [Context Command Hider](https://github.com/Mara-Li/obsidian-context-menu-hider) | `context-command-hider` | Hide any command from the right-click menu. |
| [Contextual note templating](https://github.com/Balibaloo/obsidian-contextual-note-templating) | `contextual-note-templating` | Prompts for values and templates to create notes. |
| [Contextual Sidecar](https://github.com/matthewturk/obsidian-sidecar-panel) | `contextual-sidecar` | Add a context-dependent sidecar panel. |
| [Contextual Typography](https://github.com/mgmeyers/obsidian-contextual-typography) | `obsidian-contextual-typography` | This plugin adds a data-tag-name attribute to all top-level divs in preview mode containing the child's tag name, allowing contextual typography styling. |
| [Continuous Mode](https://github.com/gasparschott/obsidian-continuous-mode) | `continuous-mode` | Displays all open notes in a tab group as if they were a continuous scrollable document (sometimes called "Scrivenings mode"). Open all notes in Continuous Mode from a folder, search results, or links in a file or Dataview/query block; use arrow keys to navigate between notes; display notes in “Compact Mode” similar to Evernote or Bear; reorder notes via tab header drag-and-drop, sorting, more. |
| [Contribution Graph](https://github.com/vran-dev/obsidian-contribution-graph) | `contribution-graph` | Generate a interactive heatmap graph to visualize and track your productivity |
| [Control Characters](https://github.com/joethei/obsidian-control-characters) | `control-characters` | Show control/non-printing characters in edit mode. |
| [Convert Base64 to PNG](https://github.com/nykkolin/obsidian-convert-base64-to-png) | `convert-base64-to-png` | Convert base64-encoded images in notes to local PNG files |
| [Convert url to preview (iframe)](https://github.com/FHachez/obsidian-convert-url-to-iframe) | `convert-url-to-iframe` | Convert an url (ex, youtube) into an iframe (preview) |
| [Cooklang](https://github.com/rveciana/obsidian-cooklang) | `cooklang-viewer-and-editor` | Display and edit recipes written in the Cooklang format. |
| [Cooklang Editor](https://github.com/cooklang/cooklang-obsidian) | `cooklang-obsidian` | Edit and display Cooklang recipes in Obsidian |
| [Cooksync](https://github.com/furst/cooksync-obsidian) | `cooksync` | Automatically imports Cooksync data. |
| [Copilot](https://github.com/logancyang/obsidian-copilot) | `copilot` | Your AI Copilot: Chat with Your Second Brain, Learn Faster, Work Smarter. |
| [Copilot auto completion](https://github.com/j0rd1smit/obsidian-copilot-auto-completion) | `copilot-auto-completion` | Adds a highly configurable copilot-like auto-completion to Obsidian using the ChatGPT API. |
| [Copy as HTML](https://github.com/jenningsb2/copy-as-html) | `copy-as-html` | This is a simple plugin that converts the selected markdown to HTML and copies it to the clipboard. |
| [Copy as Latex](https://github.com/mo-seph/obsidian-copy-as-latex) | `copy-as-latex` | Plugin to quickly copy markdown as Latex, with citations |
| [Copy As PlainText](https://github.com/FinickySpider/Obsidian-Copy-as-Plaintext) | `copy-plaintext` | Copy selections or entire notes as plain text. Both commands are available in the command palette; selection copy is also in the context menu. |
| [Copy as source](https://github.com/gapmiss/copy-as-source) | `copy-as-source` | Select and copy source HTML in reading view. |
| [Copy Block Link](https://github.com/mgmeyers/obsidian-copy-block-link) | `obsidian-copy-block-link` | Get links to blocks and headings from Obsidian's right click menu |
| [Copy document as HTML](https://github.com/mvdkwast/obsidian-copy-as-html) | `copy-document-as-html` | Copy the current document to clipboard as HTML, including images, diagrams etc... |
| [Copy Image](https://github.com/felipe-ds-lima/obsidian-copy-image-plugin) | `copy-image` | Easily copy image from Obsidian to clipboard by right clicking image. |
| [Copy Inline Code](https://github.com/ozavodny/obsidian-copy-inline-code-plugin) | `copy-inline-code` | Easily copy the contents of an inline code element with a single click. |
| [Copy Local Graph Paths](https://github.com/0melette/copy-local-graph-paths) | `copy-local-graph-paths` | Copies file paths of local graph links to clipboard. |
| [Copy Metadata](https://github.com/wenlzhang/obsidian-copy-metadata) | `copy-metadata` | Copy file metadata to clipboard. Insert copied metadata to file name. |
| [Copy Path](https://github.com/shumadrid/obsidian-copy-path) | `copy-path` | Adds context menu actions for copying the full/vault-relative path of files and folders. |
| [Copy Search URL](https://github.com/czottmann/obsidian-copy-search-url) | `obsidian-copy-search-url` | Adds a button to the search view for copying the Obsidian search URL. |
| [Copy Section](https://github.com/skztr/obsidian-plugin-section-copy) | `copy-section` | adds a Copy button to the top of Headed sections |
| [Core Search Assistant](https://github.com/qawatake/obsidian-core-search-assistant-plugin) | `obsidian-core-search-assistant-plugin` | Enhance built-in search: keyboard interface, card preview, bigger preview |
| [Countdown To](https://github.com/guicattani/obsidian-countdown-to) | `countdown-to` | Create countdown progress bars in your notes |
| [Course Module Loader](https://github.com/QuintSmart/obsidian-course-module-loader) | `course-module-loader` | Downloads and unzips course module zip files from a URL into a specified vault folder, skipping existing files. |
| [Crackboard](https://github.com/bruce-pain/crackboard-obsidian) | `crackboard` | tpot leaderboard productivity tracker |
| [Crafty](https://github.com/liolle/Crafty) | `crafty` | Add tooltip to any canvas node and Quickly navigate between canvas nodes |
| [Creases](https://github.com/liamcain/obsidian-creases) | `creases` | Tools for efficiently folding markdown sections in Obsidian |
| [create folder notes with dropdown](https://github.com/SturdyShawn/Create-folder-notes-with-dropdown) | `create-folder-notes-with-dropdown` | create-folder-notes-with-dropdown is a plugin designed to help users quickly create Markdown files in existing or nonexisting folders with dropdown. |
| [Create List of Notes](https://github.com/andrewheekin/obsidian-create-note-list) | `create-note-list` | Create a bulleted list (with links) of all notes in the current folder. |
| [Create Note in Folder](https://github.com/Mara-Li/obsidian-create-note-in-folder) | `create-note-in-folder` | Add commands to create a note in a specific folder. |
| [Create Note with Date in This Directory](https://github.com/kargnas/obsidian-create-note-with-date) | `create-note-with-date` | Create a new note with today's date in the current directory |
| [Create Task](https://github.com/simonknittel/obsidian-create-task) | `create-task` | Create tasks faster from anywhere. |
| [Cron](https://github.com/cdloh/obsidian-cron) | `cron` | Simple CRON / schedular plugin to regularly run user scripts or Obsidian commands. |
| [Crossbow](https://github.com/shoedler/crossbow) | `crossbow` | Find possible backlinks in your notes. |
| [Crosslink Advanced](https://github.com/d7sd6u/obsidian-crosslink-advanced) | `crosslink-advanced` | Tag files using folders and symlinks system (ftags). |
| [Crumbs](https://github.com/tgrosinger/crumbs-obsidian) | `crumbs-obsidian` | Breadcrumb navigation in Obsidian |
| [Crypt It](https://github.com/remotely-save/crypt-it) | `crypt-it` | Generate encrypted version of file(s) using rclone encryption format. |
| [Crypto Lookup](https://github.com/kinabalu/obsidian-crypto-lookup) | `obsidian-crypto-lookup` | A plugin for Obsidian which uses the Cryptonator API to pull back prices for crypto in a target currency |
| [Cryptsidian](https://github.com/triumphantomato/cryptsidian) | `cryptsidian` | Encrypt all files in your Obsidian.md Vault with a password. |
| [CSS Editor](https://github.com/Zachatoo/obsidian-css-editor) | `css-editor` | Edit CSS snippet files. |
| [CSS Inlay Colors](https://github.com/GRA0007/obsidian-css-inlay-colors) | `css-inlay-colors` | Show inline color hints for CSS colors |
| [CSS Inserter](https://github.com/Erallie/css-inserter) | `css-inserter` | Inserts user-defined css snippets into the selected text. |
| [css snippets](https://github.com/jdbrice/obsidian-css-snippets) | `css-snippets` | Load and manage css snippets |
| [CSV All-in-One](https://github.com/Hangeol-Chang/obsidian-csv-allinone) | `csv-allinone` | all about CSV. |
| [CSV Codeblock](https://github.com/elrindir/obsidian-csv-codeblock) | `csv-codeblock` | This is a plugin for Obsidian. This plugin renders codeblocks with csv format. |
| [CSV Editor](https://github.com/deathau/csv-obsidian) | `csv-obsidian` | Edit CSV files in Obsidian |
| [CSV Lite](https://github.com/LIUBINfighter/csv-lite) | `csv-lite` | Just open and edit CSV files directly, no more. Keep it simple. |
| [CSV Table](https://github.com/coddingtonbear/obsidian-csv-table) | `obsidian-csv-table` | Render CSV data as a table within your notes. |
| [Ctrl-XA cycle various items](https://github.com/nbossard/obsidian-CtrlXA) | `ctrl-xa` | Cycle through various items with keyboard shortcuts. Such as days, months, log level,... anything you need. |
| [Cubox](https://github.com/OLCUBO/obsidian-cubox) | `cubox-sync` | Sync your Cubox articles & annotations |
| [Current File](https://github.com/2shortplanks/current-file) | `current-file` | Allows external applications to know what file the desktop app is currently viewing. |
| [Current File Tags](https://github.com/trung-tran-swe/obsidian-current-file-tags) | `current-file-tags` | Display the active Markdown file's tags and associated files. |
| [Current Folder Notes](https://github.com/Caffa/Obsidian-Current-Folder-Note-Display-Plugin) | `current-folder-notes-pamphlet` | Shows a list of notes in the current folder, and allows you to filter the titles to include or exclude notes. |
| [Current View](https://github.com/LucEast/obsidian-current-view) | `current-view` | Automatically set the view mode (Reading, Live Preview, Source) for notes using folder rules, file patterns, or frontmatter. |
| [Cursor Bridge](https://github.com/lengff123/cursor-bridge) | `cursor-bridge` | Seamlessly bridge your notes with Cursor, the AI-powered code editor. Open notes directly in Cursor to enhance your workflow. |
| [Cursor Jump](https://github.com/LifeFi/obsidian-jump) | `cursor-jump` | Quickly jump between list items and headings throughout same or upper/lower level |
| [Cursor Location](https://github.com/spslater/obsidian-cursor-location-plugin) | `obsidian-cursor-location-plugin` | This displays the location of the cursor (character and line number). |
| [Cursor Position History](https://github.com/fgubler/obsidian-cursor-position-history) | `cursor-position-history` | Remember the previous positions of the cursor across files: auto-scroll to the correct position in a new file. Navigate backward and forward through your cursor position history without losing context. |
| [Cursor Position on Title Enter](https://github.com/chaintng/cursor-position-on-title-enter) | `cursor-position-on-title-enter` | Set the cursor position after pressing Enter on the note title. |
| [cursor-goaway](https://github.com/liuxingyu521/obsidian-plugin-cursor-goaway) | `cursor-goaway` | make cursor goaway after open a text file |
| [Custom Attachment Location](https://github.com/mnaoumov/obsidian-custom-attachment-location) | `obsidian-custom-attachment-location` | Customize attachment location with variables(${noteFileName}, ${date:format}, etc) like typora. |
| [Custom Classes](https://github.com/LilaRest/obsidian-custom-classes) | `custom-classes` | Custom Classes is a minimalist plugin that allows you to add custom HTML classes to markdown blocks |
| [Custom Commands](https://github.com/Staaaaaaaaaan/obsidian-custom-commands) | `custom-commands` | Create custom commands to be executed in the command palette, and by hotkey. Currently supports opening specific notes, creating notes, inserting snippets, and executing sequences of commands. |
| [Custom Comments](https://github.com/Jack-Chronicle/custom-comment) | `custom-comment` | Adds a method to create custom keyboard shortcuts that enclose comments. |
| [Custom File Explorer sorting](https://github.com/SebastianMC/obsidian-custom-sort) | `custom-sort` | Allows for manual and automatic, config-driven reordering and sorting of files and folders in File Explorer |
| [Custom File Extensions Plugin](https://github.com/MeepTech/obsidian-custom-file-extensions-plugin) | `obsidian-custom-file-extensions-plugin` | Associate views with custom file extensions via settings. |
| [Custom File Viewer](https://github.com/peabody28/obsidian-extension-custom-file-viewer) | `custom-file-viewer` | Open files with custom external applications based on file extension |
| [Custom Font Loader](https://github.com/pourmand1376/obsidian-custom-font) | `custom-font-loader` | Customize your Obsidian vault with any font you want (+ Support for Android and IOS) |
| [Custom Frames](https://github.com/Ellpeck/ObsidianCustomFrames) | `obsidian-custom-frames` | A plugin that turns web apps into panes using iframes with custom styling. Also comes with presets for Google Keep, Todoist and more. |
| [Custom Icons](https://github.com/Raven-Pensieve/obsidian-custom-icons) | `custom-sidebar-icons` | Enhance your workspace with customizable icons for documents and folders. |
| [Custom Image Auto Uploader](https://github.com/haierkeys/obsidian-custom-image-auto-uploader) | `custom-image-auto-uploader` | You can batch download images from your notes on desktop, iOS, and Android platforms, and batch upload and save them to a remote server, home NAS, or cloud storage (such as Alibaba Cloud OSS, Amazon S3, Cloudflare R2, MinIO). Additionally, you can stretch, crop, and resize the images. |
| [Custom list character](https://github.com/lilian-pouliquen/obsidian-custom-list-character) | `custom-list-character` | Adds the ability to choose the character to use when creating a bullet list between '-', '*' and '+' |
| [Custom new file name](https://github.com/hokolamp/obsidian-custom-new-file-name) | `custom-new-file-name` | Enables the creation of new notes with custom formatted names, including dynamic datetime stamps. |
| [Custom Node Size](https://github.com/jackvonhouse/custom-node-size) | `custom-node-size` | Customize nodes size for improved graph understanding. |
| [Custom Note Width](https://github.com/0skater0/obsidian-custom-note-width) | `custom-note-width` | Let's you adjust the line width on a note-by-note basis. |
| [Custom save](https://github.com/HananoshikaYomaru/obsidian-custom-save) | `custom-save` | Run any commands when you save a file in the editor |
| [Custom Selected Word Count](https://github.com/banisterious/obsidian-custom-selected-word-count) | `custom-selected-word-count` | Comprehensive text analysis for selected text including word counting, character counting, and sentence counting with modern UI design. |
| [Custom Slides](https://github.com/davidvkimball/obsidian-custom-slides) | `custom-slides` | Customizes the Slides core plugin navigation, styles, and behavior. |
| [Custom State for Task List](https://github.com/OkamiWong/obsidian-custom-state-for-task-list) | `custom-state-for-task-list` | Add custom states to task list items. |
| [Custom Syntax Highlights](https://github.com/Outsiders17711/Obsidian-Custom-Syntax-Highlights) | `custom-syntax-highlights` | Display files with custom extensions as syntax-highlighted code blocks in reading view with configurable extension-to-language mappings. |
| [Custom Theme Studio](https://github.com/gapmiss/custom-theme-studio) | `custom-theme-studio` | Create and customize themes with a built-in CSS editor. Modify colors, styles, and export your custom theme. |
| [Custom window title](https://github.com/jplattel/open-note-to-window-title) | `open-note-to-window-title` | Allows template-based customization of the app window title |
| [Customizable Menu](https://github.com/kzhovn/obsidian-customizable-menu) | `customizable-menu` | Allows you to add any command to Obsidian's right-click menu. |
| [CustomJS](https://github.com/saml-dev/obsidian-custom-js) | `customjs` | This plugin lets you use custom javascript files inside your vault. |
| [Cut The Fluff](https://github.com/adamfletcher/obsidian-cut-the-fluff) | `cut-the-fluff` | Make your writing clearer by checking for unnecessary complexity and clutter. |
| [Cycle In Sidebar](https://github.com/houcheng/obsidian-cycle-in-sidebar-plugin) | `cycle-in-sidebar` | This a plugin provides hotkeys to cycle through tabs in the left or right sidebars. |
| [Cypher](https://github.com/aths7/cypher) | `cypher` | Hides text in a simple diagramatic cypher to make reading unrecognizable for viewers. |
| [D2](https://github.com/terrastruct/d2-obsidian) | `d2-obsidian` | The official D2 plugin for Obsidian. D2 is a modern diagram scripting language that turns text to diagrams. |
| [Daf Yomi](https://github.com/lyonsquark/obsidian-daf-yomi) | `obsidian-daf-yomi` | Fill in Daf Yomi pages |
| [DaggerForge](https://github.com/Torutu/daggerforge) | `daggerforge` | Easy access to Daggerheart's content and creating your own. |
| [Daily Activity](https://github.com/trydalch/obsidian-daily-activity) | `daily-activity` | A collection of commands to track your writing activity. |
| [Daily Named Folder](https://github.com/NemoAndrea/obsidian-daily-named-folder) | `obsidian-daily-named-folder` | Like daily notes, but nested in a named daily folder. Better for attachment management. Includes more flexible naming. |
| [Daily News Briefing](https://github.com/ChenziqiAdam/Daily-News-Briefing) | `daily-news-briefing` | Get AI-powered daily news summaries in your vault. Features customizable topics, smart filtering, and automated scheduling. |
| [Daily Note Collector](https://github.com/LA/obsidian-daily-note-collector) | `daily-note-collector` | Adds links to new notes to your daily note. |
| [Daily note creator](https://github.com/mario-holubar/obsidian-daily-note-creator) | `daily-note-creator` | Automatically creates missing daily notes |
| [Daily Note Metrics](https://github.com/Andre-Diamond/note-metrics) | `note-metrics` | Parses tags, emoji tags, and checkboxes in your Daily Notes to create interactive charts. |
| [Daily Note Navbar](https://github.com/karstenpedersen/obsidian-daily-note-navbar) | `daily-note-navbar` | Navigate between sequential daily notes with ease. |
| [Daily Note Outline](https://github.com/iiz00/obsidian-daily-note-outline) | `obsidian-daily-note-outline` | Add a custom view which shows outline of multiple daily notes with headings, links, tags and list items |
| [Daily Note Pinner](https://github.com/lukemt/obsidian-daily-note-pinner) | `daily-note-pinner` | Pins the Daily Note of the present day. Unpinns all Daily Notes of past and future days. |
| [Daily Note Structure](https://github.com/db-developer/daily-note-structure) | `daily-note-structure` | One-Click create a structure for and including your daily notes. |
| [Daily Notes Automater](https://github.com/davidpedrero/obsidian-daily-notes-automater) | `daily-note-automater` | Automates the creation of a daily note |
| [Daily notes calendar](https://github.com/bartkessels/daily-note-calendar) | `daily-note-calendar` | Navigate your Obsidian Vault using a calendar view. |
| [Daily Notes Editor](https://github.com/Quorafind/Obsidian-Daily-Notes-Editor) | `daily-notes-editor` | Edit a bunch of daily notes in one page(inline), which works similar to Roam Research's default daily note view. |
| [Daily notes opener](https://github.com/reorx/obsidian-daily-notes-opener) | `obsidian-daily-notes-opener` | Easily open daily/periodic notes in new pane, and much more! |
| [Daily Notes Tweaks](https://github.com/coignard/obsidian-daily-notes-tweaks) | `daily-notes-tweaks` | Open a random daily note and automatically switch past daily notes to reading mode. |
| [Daily Notes Viewer](https://github.com/johnsonhong997/obsidian-daily-notes-viewer) | `obsidian-daily-notes-viewer` | Help you to view some recent daily notes on one page. |
| [Daily Prompt](https://github.com/Erl-koenig/obsidian-dailyPrompt) | `daily-prompt` | Set up custom prompts and automatically fill them into your daily notes |
| [Daily Random Note](https://github.com/D4rkP1xel/daily-random-note) | `daily-random-note` | Automatically open daily random notes based on your preferences. |
| [Daily Routine](https://github.com/sechan100/daily-routine-2) | `daily-routine` | Manage your daily tasks as 'Routine' and organize your everyday life more effectively. |
| [Daily Statistics](https://github.com/yefengr/obsidian-daily-statistics) | `daily-statistics` | Count the number of words written each day and display it on a calendar. |
| [Daily Stats](https://github.com/dhruvik7/obsidian-daily-stats) | `obsidian-daily-stats` | Track your daily word count across all notes in your vault. |
| [Daily Summary](https://github.com/CSLukkun/ob_daily_summary) | `daily-summary` | Auto generate daily summary |
| [Daily Task Auto Generator](https://github.com/maigamo/Daily-Task-Auto-Generator) | `daily-task-auto-generator` | Automatically generate daily tasks in specified folders with custom templates |
| [Dangerous Mode](https://github.com/vanshkumar/dangerous-obsidian) | `dangerous-mode` | Dangerous writing mode: keep typing or after 5 seconds of inactivity the current note is erased. |
| [Dangerzone Writing](https://github.com/akaalias/dangerzone-writing-plugin) | `dangerzone-writing-plugin` | “Elegant”, “Dangerous”, “Relaxing”, “Perverted”, “Your best friend”, “Your worst nightmare”. When you start a Dangerzone session, you have to write without stopping for X seconds. If you stop, think and look around, after Y seconds the plugin will DELETE what you've written in this note. |
| [Dangling links](https://github.com/graydon/obsidian-dangling-links) | `obsidian-dangling-links` | This plugin shows any dangling links in your vault. |
| [Dashing cursor](https://github.com/9r0x/obsidian-dashing-cursor) | `obsidian-dashing-cursor` | Enables dashing cursor that follows the page scroll |
| [Data Entry](https://github.com/waynevanson/data-entry-obsidian-plugin) | `data-entry` | Create forms that save data simply; the data view of data entry |
| [Data Fetcher](https://github.com/qf3l3k/obsidian-data-fetcher) | `data-fetcher` | Fetch data from multiple sources (REST APIs, RPC, gRPC, GraphQL) and insert results into notes |
| [Data Files Editor](https://github.com/ZukTol/obsidian-data-files-editor) | `data-files-editor` | Plugin to edit data files like txt, xml, json, and yaml |
| [DataCards](https://github.com/Sophokles187/data-cards) | `data-cards` | Transform Dataview query results into visually appealing, customizable card layouts. |
| [Datacore](https://github.com/blacksmithgu/datacore) | `datacore` | Reactive query engine backed by Javascript or a custom query language. |
| [Dataview](https://github.com/blacksmithgu/obsidian-dataview) | `dataview` | Complex data views for the data-obsessed. |
| [Dataview (to) Properties](https://github.com/Mara-Li/obsidian-dataview-properties) | `dataview-properties` | Automagically copy dataview inline field (and their values, even calculated!) into frontmatter properties and keep them sync. |
| [Dataview Autocompletion](https://github.com/dnlbauer/obsidian-dataview-autocompletion) | `dataview-autocompletion` | Adds autocompletion to Dataview metadata fields |
| [Dataview Publisher](https://github.com/udus122/dataview-publisher) | `dataview-publisher` | Output markdown from your Dataview queries and keep them up to date. You can also publish them. |
| [Dataview Serializer](https://github.com/dsebastien/obsidian-dataview-serializer) | `dataview-serializer` | Serialize Dataview queries to Markdown, and keep the Markdown representation up to date. |
| [Date Inserter](https://github.com/namikaze-40p/obsidian-date-inserter) | `date-inserter` | Insert a date at the cursor position using a calendar. |
| [Date Range Expander](https://github.com/mildeveloper/obsidian-date-range-expander) | `date-range-expander` | Quickly add a range of day references given a date duration. |
| [Datepicker](https://github.com/joycode-hub/datepicker-plugin) | `datepicker` | Use a date picker to modify and insert date/time anywhere in your markdown notes. |
| [Datetime Language Changer](https://github.com/ZetabS/datetime-language-changer) | `datetime-language-changer` | Customize the language used for datetime formatting by changing moment.js's locale. |
| [Day and Night](https://github.com/CyberT17/obsidian-day-and-night) | `obsidian-day-and-night` | An Obsidian plugin to automatically toggle themes between day theme and night theme on a set time schedule. |
| [Day One Importer](https://github.com/MarcDonald/obsidian-day-one-importer) | `day-one-importer` | Import Day One journals |
| [Day Planner](https://github.com/ivan-lednev/obsidian-day-planner) | `obsidian-day-planner` | A day planner with clean UI and readable syntax |
| [Day Planner (OG)](https://github.com/ebullient/obsidian-day-planner-og) | `day-planner-og` | A plugin to help you plan your day and setup pomodoro timers; fork of the original plugin by James Lynch (which stopped at 0.5.8) which preserves the look/feel and behavior of the original. |
| [Days Since](https://github.com/gndclouds/days-since-obsidian) | `days-since` | A plugin to show the number of days since a given date. |
| [Decks](https://github.com/dscherdi/decks) | `decks` | Decks - Spaced repetition flashcards plugin with FSRS algorithm. |
| [DeepL](https://github.com/friebetill/obsidian-deepl) | `deepl` | Allows translation of selected texts into more than 25 languages with DeepL. |
| [deepseek-ai-assistant](https://github.com/mali-i/deepseek-ai-assistant) | `deepseek-ai-assistant` | Help you to study with ai-prompting. |
| [Default New Tab Page](https://github.com/chrisgrieser/new-tab-default-page) | `new-tab-default-page` | Open a note of your choice when creating a new tab, like in the browser. |
| [Default query in backlinks](https://github.com/Benature/obsidian-default-query-in-backlink) | `default-query-in-backlink` | Automatically input default query in search input of backlinks in document. |
| [Default Template](https://github.com/raeperd/obsidian-default-template) | `default-template` | Automatically apply templates to new notes with user-configurable template selection. |
| [Definition List](https://github.com/shammond42/definition-list) | `definition-list` | Adds definition lists to the markdown parser. |
| [Dendron Tree](https://github.com/levirs565/obsidian-dendron-tree) | `dendron-tree` | Add tree for exploring Dendron note. |
| [Desci](https://github.com/Obsidian-Desci/Obsidian-Desci) | `desci` | A collection of tools that integrate obsidian with web3. |
| [Desk](https://github.com/davidlandry93/obsidian-desk) | `desk` | A desk to see notes at a glance in Obsidian. Requires Dataview as a dependency. |
| [Desmos](https://github.com/Nigecat/obsidian-desmos) | `obsidian-desmos` | Embed Desmos graphs into your notes |
| [DEVONlink](https://github.com/ryanjamurphy/DEVONlink-obsidian) | `DEVONlink-obsidian` | Open or reveal the current note in DEVONthink. |
| [DevOps Companion](https://github.com/jkom4/obsidian-devops-compagnon) | `devops-companion` | Document infrastructure as clearly as you build it. |
| [Diagram Popup](https://github.com/gitcpy/obsidian-diagram-popup) | `mermaid-popup` | Show diagrams, from Mermaid, PlantUML, Graphviz and so on, in a draggable and zoomable popup |
| [Diagrams](https://github.com/zapthedingbat/drawio-obsidian) | `drawio-obsidian` | Draw.io diagrams for Obsidian. This plugin introduces diagrams that can be included within notes or as stand-alone files. Diagrams are created as SVG files (although .drawio extensions are also supported). |
| [Diagrams.net](https://github.com/jensmtg/obsidian-diagrams-net) | `obsidian-diagrams-net` | Enable diagrams.net (previously draw.io) type diagrams, with the diagrams.net embedded editor. |
| [Dialogue](https://github.com/holubj/obsidian-dialogue-plugin) | `obsidian-dialogue-plugin` | Create dialogues in Markdown. |
| [Dialogue Mode](https://github.com/patrickchiang/obsidian-dialogue-mode) | `dialogue-mode` | Dialogue mode for editing speech in writing. |
| [Diarian](https://github.com/Erallie/diarian) | `diarian` | All-in-one journaling toolkit. |
| [Diary ICS](https://github.com/mousebomb/obsidian-diary-ics) | `diary-ics` | Sync diary entries to system calendar via ICS feed. |
| [Dice Roller](https://github.com/javalent/dice-roller) | `obsidian-dice-roller` | Inline dice rolling for Obsidian.md |
| [Dictionary](https://github.com/phibr0/obsidian-dictionary) | `obsidian-dictionary-plugin` | This is a simple dictionary for the Obsidian Note-Taking Tool. |
| [Dictionary Lexicon](https://github.com/st-vin/obsidian-lexicon-dictionary-plugin) | `lexicon-dictionary` | Look up words and improve vocabulary by using flash card style cards. |
| [Dictionary translator](https://github.com/grover572/obsidian-Dictionary-translator) | `dictionary-translator` | 它可以帮助你翻译单词或句子，听新单词或句子的录音，甚至录下自己的发音，以内部链接的形式保存到你的笔记中。 |
| [Differential ZIP Backup](https://github.com/vrtmrz/diffzip) | `diffzip` | Back our vault up with lesser storage. |
| [Digital Garden](https://github.com/oleeskild/obsidian-digital-garden) | `digitalgarden` | Publish your notes to the web for others to enjoy. For free. |
| [digital paper](https://github.com/danferns/digital-paper-obsidian-plugin) | `digital-paper` | turn off backspace and undo, just like writing with a pen on real paper. |
| [Dirtreeist](https://github.com/k4a-l/obsidian-dirtreeist) | `obsidian-dirtreeist` | Render a directory Structure Diagram from a markdown lists in codeblock. |
| [Disable Tabs](https://github.com/davidvkimball/obsidian-disable-tabs) | `disable-tabs` | Disables having more than one tab open at a time. |
| [Disciples Journal](https://github.com/scottTomaszewski/obsidian-disciples-journal) | `disciples-journal` | Embed Bible references and passages in your notes and read the Bible in Obsidian. |
| [Discord Message Formatter](https://github.com/Emile-Durkheim/obsidian_discord_formatter) | `discord-message-formatter` | Simply CTRL+C CTRL+V Discord messages from the Desktop client and have them automatically formatted |
| [Discord Message Sender](https://github.com/okawak/discord_message_sender) | `discord-message-sender` | Send messages from a Discord channel to your Vault |
| [Discord Rich Presence](https://github.com/lukeleppan/obsidian-discordrpc) | `obsidian-discordrpc` | Update your Discord Status to show your friends what you are working on in Obsidian. With Discord Rich Presence. |
| [Discord Timestamps](https://github.com/Erallie/discord-timestamps) | `discord-timestamps` | Displays discord timestamps in read mode as they would appear in Discord. |
| [Discordian Theme](https://github.com/radekkozak/discordian-plugin) | `discordian-plugin` | Discordian plugin for tweaking Discordian theme |
| [Discrete](https://github.com/shkarlsson/obsidian-discrete) | `discrete` | Filter files in the file explorer based on their frontmatter metadata |
| [Disk Usage](https://github.com/Promptier/disk-usage) | `disk-usage` | Measures disk usage for tracking size of folders and file types. |
| [Display Relative Path Img](https://github.com/dyc2424748461/obsidian-display-relative-path-img) | `display-relative-path-img` | Display the image of the <img> tag |
| [Divide & Conquer](https://github.com/chrisgrieser/obsidian-divide-and-conquer) | `obsidian-divide-and-conquer` | Provides commands for bulk enabling/disabling of plugins. Useful for debugging when you have many plugins. |
| [DMN](https://github.com/joleaf/obsidian-dmn-plugin) | `dmn-plugin` | This plugin enables viewing DMNs using dmn-js. |
| [DMN Eval](https://github.com/joleaf/obsidian-dmn-eval-plugin) | `dmn-eval` | This plugin enables evaluating DMNs in an obsidian note. |
| [DocBase (Unofficial)](https://github.com/kuvanov-2/obsidian-docbase) | `docbase-unofficial` | Pull and push notes to DocBase |
| [Docusaurus Style Admonitions](https://github.com/rwbr/obsidian-docusaurus-style-admonitions) | `docusaurus-style-admonitions` | Adds Docusaurus style admonitions |
| [DOCX Exporter](https://github.com/kanshurichard/obsidian-docx-exporter) | `docx-exporter` | Export notes to Microsoft Word docx files with mobile devices support. |
| [Docxer](https://github.com/Developer-Mike/obsidian-docxer) | `docxer` | Import Word files easily. Adds a preview mode for .docx files and the ability to convert them to markdown (.md) files. |
| [doing](https://github.com/Rooyca/doing) | `doing` | It helps you remember what you were doing. |
| [Douban](https://github.com/Wanxp/obsidian-douban) | `obsidian-douban-plugin` | This is a plugin that can import movies/books/musics/notes/games info data from Douban for Obsidian . |
| [Double Colon Conceal](https://github.com/msrch/obsidian-double-colon-conceal) | `double-colon-conceal` | Display double colon (i.e. Dataview inline fields) as a single colon for more natural reading experience. |
| [Double row toolbar](https://github.com/lorens-osman-dev/double-row-toolbar) | `double-row-toolbar` | Adds a second row to the toolbar on mobile devices, allowing for more quick access buttons. |
| [Double-Click Image Opener](https://github.com/atman-33/double-click-image-opener) | `double-click-image-opener` | Open images with your system's default application by double-clicking. |
| [Doubleshift](https://github.com/Qwyntex/doubleshift) | `obsidian-doubleshift` | Open the command palette by pressing Shift (or any other key) twice like in IntelliJ and create your own shortcuts |
| [downloadPDF](https://github.com/frieda21/downloadPDF) | `downloadpdf` | Allows you to download all included PDF files |
| [Draft Indicator](https://github.com/beardicus/obsidian-draft-indicator-plugin) | `draft-indicator` | Show draft status with ✎ icons in the file explorer. |
| [Drag To Scroll](https://github.com/constsz/obsidian-drag-to-scroll) | `drag-to-scroll` | Drag to scroll - just like on a touch device. |
| [Draw Harada Method](https://github.com/yildbs/obsidian-harada-method-plugin) | `draw-harada-method` | This plugin is used to draw the harada method. Create your own 1 goal, 8 plans, and 64 actions |
| [Draw Steel Elements](https://github.com/SteelCompendium/draw-steel-elements) | `draw-steel-elements` | Components to support the Draw Steel TTRPG by MCDM. |
| [Draw Steel Retainer](https://github.com/MartinDampier/draw-steel-retainer) | `draw-steel-retainer` | Provides Director facing sidebar tools for the TTRPG Draw Steel |
| [Dropbox Photo Grid](https://github.com/alimoeeny/obsidian-dropbox-photo-grid) | `dropbox-photo-grid` | Display and embed photos from your Dropbox account in a customizable grid layout |
| [Due When](https://github.com/andrewbaxter439/due-when) | `due-when` | This adds shortcuts to insert due dates for end of this week or end of next week. |
| [Duplicate Detector](https://github.com/Wishmater/obsidian-plugin-duplicate-detector) | `duplicate-detector` | Highlights duplicate lines in the open note. |
| [Duplicate line](https://github.com/msztolcman/obsidian-duplicate-line) | `duplicate-line` | Duplicate line or selection |
| [Dust Calendar](https://github.com/a-nano-dust/dust-obsidian-calendar) | `dust-calendar` | 更符合中国习惯的日历，可以显示农历、节气、节假日、调休信息，支持月视图和年视图切换，支持关联创建周期性笔记。 |
| [Dynamic Background](https://github.com/samuelsong70/obsidian-dynamic-background) | `obsidian-dynamic-background` | Adding dynamic effects and/or static wallpapers for Obsidian background |
| [Dynamic Embed](https://github.com/dabravin/obsidian-dynamic-embed) | `obsidian-dynamic-embed` | Dynamicly interpreted inline embeds. |
| [Dynamic Highlights](https://github.com/nothingislost/obsidian-dynamic-highlights) | `obsidian-dynamic-highlights` | Dynamically highlight text based on cursor selection or search query with full regex, mobile, and live preview support |
| [Dynamic Line Height for CJK](https://github.com/RyotaUshio/obsidian-dynamic-line-height-cjk) | `dynamic-line-height-cjk` | Dynamically adjust line height for lines & paragraphs containing CJK characters. |
| [Dynamic Outline](https://github.com/theopavlove/obsidian-dynamic-outline) | `dynamic-outline` | Adds a customizable GitHub-like floating table of contents. |
| [Dynamic Text Concealer](https://github.com/mattcoleanderson/obsidian-dynamic-text-concealer) | `dynamic-text-concealer` | Conceal or replace user configured text patterns in Live Preview and Read Mode. |
| [Dynamic Timetable](https://github.com/L7Cy/obsidian-dynamic-timetable) | `dynamic-timetable` | Calculate the estimated time of completion from the estimated time of the task and dynamically create a timetable. |
| [Dynbedded](https://github.com/MMoMM-org/obsidian-dynbedded) | `obsidian-dynbedded` | Dynamic Embeds for Obsidian.md |
| [e-Daiary](https://github.com/wholetomy/obsidian-e-daiary) | `e-daiary` | Creates directories and notes based on the day of the year. |
| [Ear Training](https://github.com/shiwer/ear-training-obsidian-plugin) | `ear-training` | Get ear training exercises inside your vault. |
| [Easy Bake](https://github.com/obsidian-community/obsidian-easy-bake) | `easy-bake` | Easily compile many Obsidian notes down to a single file. |
| [Easy Copy](https://github.com/Moyf/easy-copy) | `easy-copy` | Easily copy the text within inline code, bold text (and many other formats), or quickly generate an elegant link to a heading. |
| [Easy Fonts](https://github.com/jose-elias-alvarez/obsidian-easy-fonts) | `easy-fonts` | Easily load custom fonts, even on mobile. |
| [Easy Keep View](https://github.com/tazihad/obsidian-easy-keep-view) | `easy-keep-view` | Easy Keep View mimics the Google Keep interface, allowing you to view and manage your notes with image thumbnails and excerpts. |
| [Easy Test](https://github.com/forrest1398/obsidian-easyTest-plugin) | `easy-test` | Easily create simple tests |
| [Easy Timeline](https://github.com/Romelium/obsidian-easy-timeline) | `easy-timeline` | Simplifies creating and visualizing timelines from text using dates and metadata |
| [Easy Tracker](https://github.com/hunter-ji/obsidian-easy-tracker) | `easy-tracker` | Instantly track goals and habits. Simple, beautiful, and configuration-free. |
| [Easy Typing](https://github.com/Yaozhuwa/easy-typing-obsidian) | `easy-typing-obsidian` | This plugin aims to enhance and optimize the editing experience in Obsidian |
| [EasyLink](https://github.com/isitwho/EasyLink) | `easylink` | Select text in your editor to find the most similar content from other notes and easily create links. |
| [Eccirian Encrypt](https://github.com/Enthalpiex/Eccirian-Encrypt) | `eccirian` | Next-generation file encryption solution based on modern cryptography. |
| [Edge TTS](https://github.com/travisvn/obsidian-edge-tts) | `edge-tts` | Read notes aloud using Microsoft Edge Read Aloud API (free, high quality text-to-speech). |
| [Edit Gemini](https://github.com/Basil-Mori/obsidian-edit-gemini) | `edit-gemini` | Allows the user to edit and create .gmi files. |
| [Edit History](https://github.com/antoniotejada/obsidian-edit-history) | `edit-history` | Automatically saves the history of edits of a file when Obsidian saves the file, and allows viewing the differences between edits, copying text from a previous edit, or fully rolling back to a previous edit. |
| [Edit in Neovim](https://github.com/TheseusGrey/edit-in-neovim) | `edit-in-neovim` | Open a Neovim buffer for the currently open file |
| [Edit Link Alias](https://github.com/mnaoumov/obsidian-edit-link-alias) | `edit-link-alias` | Adds edit link alias command. |
| [Edit MDX](https://github.com/timppeters/obsidian-edit-mdx) | `edit-mdx` | Allows the user to edit and create .mdx files. |
| [Edit mode switch](https://github.com/Mara-Li/obsidian-edit-shortcut) | `shortcut-edit-mode` | Add a button in file header in edit mode, to switch between source & live-preview |
| [Editing Mode Hotkey](https://github.com/Signynt/obsidian-editing-mode-hotkey) | `editing-mode-hotkey` | Adds a command and hotkey to toggle the default editing mode (between Live Preview and Source) |
| [Editing Toolbar](https://github.com/PKM-er/obsidian-editing-toolbar) | `editing-toolbar` | The Obsidian Editing Toolbar is modified from cmenu, which provides more powerful customization settings and has many built-in editing commands to be a MS Word-like toolbar editing experience. |
| [Editor Autofocus](https://github.com/mgussekloo/obsidian-editor-autofocus) | `editor-autofocus` | Autofocus the editor when opening a new file. |
| [Editor Commands Remap](https://github.com/c4ctus5/editor-commands-remap) | `editor-commands-remap` | Map hotkeys to editor commands. |
| [Editor Width Slider](https://github.com/MugishoMp/obsidian-editor-width-slider) | `editor-width-slider` | Customize Obsidian's editor width with a slider for a tailored editing experience. |
| [Efficient Word Count](https://github.com/blueheron786/obsidian-efficient-word-count) | `efficient-word-count` | Efficiently calculates and caches word counts for notes, with folder exclusion. Uses cache to avoid recalculating word counts for unchanged notes. |
| [Ego Rock](https://github.com/echo-bravo-yahoo/ego-rock) | `ego-rock` | A basic taskwarrior UI for listing and modifying tasks. |
| [Electron Window Tweaker](https://github.com/mgmeyers/obsidian-electron-window-tweaker) | `obsidian-electron-window-tweaker` | Tweak various Electron window settings. |
| [Eleven Labs](https://github.com/veritas1/eleven-labs-obsidian-plugin) | `eleven-labs` | Turn your Obsidian notes into text-to-speech audio files with Eleven Labs. |
| [Emacs text editor](https://github.com/Klojer/obsidian-emacs-text-editor) | `emacs-text-editor` | Partial emulation of Emacs text editor for Obisidian |
| [Email code block](https://github.com/joleaf/obsidian-email-block-plugin) | `email-block-plugin` | This plugin renders an email code block. |
| [Email Reader](https://github.com/pulsovi/obsidian_eml_reader) | `eml-reader` | Provide a preview mode for embeded `*.eml` files. |
| [Embed 3D](https://github.com/ElmoNeedsArson/Obsidian-3D-embed) | `3d_embeds` | Embed and view 3DModels in markdown notes. Supports .stl, .obj, 3mf, fbx and .gltf/.glb files. |
| [Embed Code File](https://github.com/almariah/embed-code-file) | `embed-code-file` | This is a plugin for Obsidian that allows for embedding code files. |
| [Embedded Code Title](https://github.com/tadashi-aikawa/obsidian-embedded-code-title) | `obsidian-embedded-code-title` | This is an Obsidian plugin which can embeds title to code blocks. |
| [Emo](https://github.com/yaleiyale/obsidian-emo-uploader) | `emo-uploader` | Embed markdown online file/image links. This plugin is for uploading images to hosting or files to github in Obsidian. |
| [Emoji Autocomplete](https://github.com/KraXen72/obsidian-emoji-autocomplete) | `emoji-autocomplete` | Smart suggestions when typing emoji shortcodes & more! :star: |
| [Emoji Magic](https://github.com/SimplGy/obsidian-emoji-magic) | `emoji-magic` | Easily add emoji, with a powerful keyword search. 🔮 ✨ 🐇 |
| [Emoji Picker](https://github.com/alifa98/obsidian-emoji-picker) | `emoji-picker` | An Emoji Picker that allows you to insert the latest released emojis in your notes. |
| [Emoji selector](https://github.com/infinitesum/obsidian-emoji-selector) | `emoji-selector` | Insert custom emojis with quick search, auto-suggestions, and customizable templates. |
| [Emoji Shortcodes](https://github.com/phibr0/obsidian-emoji-shortcodes) | `emoji-shortcodes` | This Plugin enables the use of Markdown Emoji Shortcodes :smile: |
| [Emoji Titler](https://github.com/HyeonseoNam/obsidian-emoji-titler) | `emoji-titler` | This plugin is emoji titler to easily insert an emoji in the title using a keyboard shortcut. |
| [Emoji Toolbar](https://github.com/oliveryh/obsidian-emoji-toolbar) | `obsidian-emoji-toolbar` | Quickly search for and insert emojis into your notes. |
| [EmoTagsTitler](https://github.com/Cyfine/EmoTagsTitler) | `emoji-tags-titler` | Add the emojis contained in the tags to the beginning of the note title. |
| [Emotion Picker](https://github.com/dartungar/obsidian-emotion-picker) | `obsidian-emotion-picker` | A plugin for Obsidian.md that lets you choose an emotion from a list to insert into a note. |
| [Encoder/Decoder](https://github.com/rudimuc/obsidian-coder) | `coder` | Converts texts into other formats (base16, base64, base85, ROT13, atbash) and vice versa |
| [Enhance Copy Note](https://github.com/kzhovn/copy-command-obsidian) | `copy-note` | Augments native Obsidian note copying. |
| [Enhance YouTube Links](https://github.com/Git-Sum/obsidian-enhance-youtube-links) | `enhance-youtube-links` | Get metadata from a YouTube video |
| [Enhanced Annotations](https://github.com/ycnmhd/obsidian-enhanced-annotations) | `enhanced-annotations` | Add a sidebar view for comments and highlights. |
| [Enhanced Canvas](https://github.com/RobertttBS/obsidian-enhanced-canvas) | `enhanced-canvas` | When creating links on Canvas, automatically add properties and Markdown links to notes. A command automatically creates canvas links based on Markdown links, and it adjusts all links to use the shortest path. |
| [Enhanced Copy](https://github.com/Mara-Li/obsidian-enhanced-copy) | `enhanced-copy` | Copy your selection and add it some edit to paste in other markdown software. Allows to keep markdown in reading view, removing wikilinks in editing, copy from locked canvas, and more! |
| [Enhanced Image](https://github.com/situ2001/obsidian-enhanced-image) | `enhanced-image` | Enhance the experience of image seamlessly. For example, operations for image in context menu, command palette. |
| [Enhanced Publisher](https://github.com/chararch/obsidian-enhanced-publisher) | `enhanced-publisher` | 增强发布插件，支持图片自动存储、HTML预览和发布到微信公众号等内容平台 |
| [Enhanced tables](https://github.com/pistacchio/obsidian-enhanced-tables) | `enhanced-tables` | Add programmable controls to selected tables |
| [Enhancing Export](https://github.com/mokeyish/obsidian-enhancing-export) | `obsidian-enhancing-export` | This is a enhancing export plugin for Obsidian. It allows to export to formats like Html, DOCX, ePub and PDF or Markdown(Hugo) etc. |
| [Enhancing Mindmap](https://github.com/MarkMindCkm/obsidian-enhancing-mindmap) | `obsidian-enhancing-mindmap` | This is a enhancing mindmap plugin for Obsidian. You can edit mindmap on markdown. |
| [Enlightenment ✨](https://github.com/ryanjamurphy/enlightenment-obsidian) | `enlightenment-obsidian` | Pay attention to what you're paying attention to. Enlightenment adds a 'zen mode' for Preview, hiding the contents of your notes except for what's underneath your pointer. |
| [Entity Linker](https://github.com/Ankush-Chander/obsidian-entity-linker) | `entity-linker` | Link research terms to standard entities |
| [Enveloppe](https://github.com/Enveloppe/obsidian-enveloppe) | `obsidian-mkdocs-publisher` | Enveloppe helps you to publish your notes on a preconfigured GitHub repository, for free, and more! |
| [Enzyme](https://github.com/jshph/obsidian-enzyme) | `reason` | a REPL to digest your thoughts |
| [Epiphany](https://github.com/Epiphany-Notes/epiphany-obsidian-plugin) | `epiphany` | Synchronize voice notes from the Epiphany app directly into your vault |
| [Epub Importer](https://github.com/aoout/obsidian-epub-importer) | `epub-importer` | Import EPUB files as Markdown. |
| [ePub Reader](https://github.com/caronchen/obsidian-epub-plugin) | `obsidian-epub-plugin` | This is an ePub reader plugin for Obsidian. Can open document with ".epub" file extension. |
| [Etherpad](https://github.com/egradman/obsidian-etherpad-lite) | `obsidian-etherpad-plugin` | Etherpad Integration |
| [Etymology Lookup](https://github.com/clairefro/obsidian-plugin-etymology-lookup) | `etymology-lookup` | Get the etymology of words in your notes |
| [EUpload](https://github.com/Appleec/e-obsidian-upload-plugin) | `e-upload` | Support uploading files to different platforms. |
| [Event Highlight](https://github.com/playmean/obsidian-event-highlight-plugin) | `event-highlight` | Render colored bars with relative event dates |
| [Evernote Decryptor](https://github.com/rcmdnk/obsidian-evernote-decryptor) | `evernote-decryptor` | Obsidian Plugin for encrypted data imported from Evernote. |
| [Every Day Calendar](https://github.com/Sporarum/every-day-calendar) | `every-day-calendar` | Create calendars inspired by Simone Giertz's Every Day Calendar |
| [Everyday Classical Music](https://github.com/Eloliuyx/everyday-classical-music-plugin) | `everyday-classical-music` | Display a different piece of classical music each day with a YouTube link in your daily note. |
| [ExcaliBrain](https://github.com/zsviczian/excalibrain) | `excalibrain` | A clean, intuitive and editable graph view for Obsidian |
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin) | `obsidian-excalidraw-plugin` | Sketch Your Mind. An Obsidian plugin to edit and view Excalidraw drawings. Enter the world of 4D Visual PKM. |
| [Excalidraw CN](https://github.com/korbinzhao/obsidian-excalidraw-cn-plugin) | `excalidraw-cn` | 支持中文手写效果的 Excalidraw。Excalidraw supporting Chinese hand write font by default. |
| [Excel](https://github.com/ljcoder2015/obsidian-excel) | `excel` | Create spreadsheets and easily embed them in Markdown |
| [Excel to Markdown Table](https://github.com/ganesshkumar/obsidian-excel-to-markdown-table) | `obsidian-excel-to-markdown-table` | An Obsidian plugin to paste data from Microsoft Excel, Google Sheets, Apple Numbers and LibreOffice Calc as Markdown tables in Obsidian editor. |
| [Execute Code](https://github.com/twibiral/obsidian-execute-code) | `execute-code` | Allows you to execute code snippets within a note. Support C, C++, Python, R, JavaScript, TypeScript, LaTeX, SQL, and many more. |
| [Exercises](https://github.com/AlexCCavaco/obsidian-exercises) | `exercises` | Create Interactive Exercises along side your Obsidian Notes |
| [ExMemo Assistant](https://github.com/exmemo-ai/obsidian-exmemo-assistant) | `exmemo-assistant` | Using LLMs to manage files and generating metadata such as tags and summaries. |
| [ExMemo Client](https://github.com/exmemo-ai/obsidian-exmemo-client) | `exmemo-client` | A client for the ExMemo service, used to search, sync, and organize data from the server. |
| [ExMemo Tools](https://github.com/exmemo-ai/obsidian-exmemo-tools) | `exmemo-tools` | Use LLMs for smart document management and optimization, including relocating files, enhancing text, and generating metadata. |
| [Expiration-Date-Tracker](https://github.com/Raboro/obsidian-expiration-date-tracker-plugin) | `expiration-date-tracker` | Keep track of all expiration dates, for example, for your groceries. |
| [Explain Selection With AI](https://github.com/BWurster/explain-selection-with-ai) | `explain-selection-with-ai` | Use an OpenAI Chat Completion API-compatible LLM endpoint to explain the selected text in greater detail. |
| [Explorer Colors](https://github.com/VaguelyElectric/obsidian-explorer-colors) | `explorer-colors` | Allows for files and folders to be configured with custom colors and other settings. |
| [Explorer Hider](https://github.com/Mara-Li/obsidian-explorer-hider) | `explorer-hider` | Hide a file or a folder from the explorer (and bookmarks) using a little bit of auto-managed CSS! |
| [Export Graph View](https://github.com/seantiz/obsidian_egv_plugin) | `export-graph-view` | Export your vault's graph view to mermaid and dot format. |
| [Export Image plugin](https://github.com/zhouhua/obsidian-export-image) | `obsidian-export-image` | Easily convert your article to image. |
| [Export to HTML](https://github.com/kalvn/obsidian-export-to-html) | `export-to-html` | Export your Markdown notes as HTML, directly in the clipboard or as a file. |
| [Export To TeX](https://github.com/raineszm/obsidian-export-to-tex) | `obsidian-export-to-tex` | Export vault files in a format amenable to pasting into a tex document |
| [Extended File Support](https://github.com/Nick-de-Bruin/obsidian-extended-file-support) | `extended-file-support` | Adds file support for various file types. Allows viewing and embedding these filetypes. Includes: .kra, .psd, .obj, .glb, .gltf, and more. |
| [Extended Graph](https://github.com/ElsaTam/obsidian-extended-graph) | `extended-graph` | Extends the features of the core Graph view, display images, manage states, remove links, change node shapes, and more. |
| [Extended Markdown Syntax](https://github.com/kotaindah55/extended-markdown-syntax) | `extended-markdown-syntax` | Extend your Markdown syntax using delimiters instead of HTML tags, such as underlining, superscript, subscript, highlighting, and spoiler. |
| [Extended MathJax](https://github.com/wei2912/obsidian-latex) | `obsidian-latex` | Adds support for a MathJax preamble and enables additional MathJax extensions for specific domains (chemistry, proofs). |
| [Extended Task Lists](https://github.com/joeriddles/extended-task-lists) | `extended-task-lists` | Extended reader view support for task lists, including in-progress and won't do task items. |
| [External File Card](https://github.com/James-Yu/external-file-card) | `external-file-card` | Display file cards for external files. |
| [External File Embed and Link](https://github.com/oylbin/obsidian-external-file-embed-and-link) | `external-file-embed-and-link` | Embed and link local files outside your vault with relative paths for cross-device and multi-platform compatibility. |
| [External File Linker](https://github.com/Kay607/obsidian-pathlinker) | `pathlinker` | Embed external files into your notes. |
| [External Link Helper](https://github.com/nakalsio/obsidian-danpung) | `obsidian-extlnkhelper-plugin` | This is a plugin for making entering external links easier. |
| [External Link Opener](https://github.com/zorazrr/obsidian-link-opener) | `obsidian-link-opener` | Open external links within Obsidian using a modal or a tab. |
| [External Links](https://github.com/jivimberg/external-links) | `external-links` | List external links and discover which notes reference them. |
| [External Links View](https://github.com/theamritanair/obsidian-external-links) | `external-links-view` | View all external links from your notes in one organized place, sorted by their source notes. |
| [External Rename Handler](https://github.com/mnaoumov/obsidian-external-rename-handler) | `external-rename-handler` | Handles renames made outside of the app |
| [Extract Highlights](https://github.com/akaalias/extract-highlights-plugin) | `extract-highlights-plugin` | Create, extract and leverage your markdown highlights |
| [Extract PDF Annotations](https://github.com/munach/obsidian-extract-pdf-annotations) | `obsidian-extract-pdf-annotations` | Extract PDF Annotations (text, highlight, underline, squiggle, free text, etc.) from files inside and outside the vault and sort them by topics |
| [Extract url content](https://github.com/trashhalo/obsidian-extract-url) | `extract-url` | Extract url converting content into markdown |
| [Fantasy Content Generator](https://github.com/Gregory-Jagermeister/Fantasy-Content-Generator) | `fantasy-content-generator` | A Fantasy Content Generator for Obsidian for All Your TTRPG / World Building Needs |
| [Fantasy name generator](https://github.com/Lukewh/fantasy-name) | `fantasy-name` | Insert a random fantasy name. |
| [Fantasy Statblocks](https://github.com/javalent/fantasy-statblocks) | `obsidian-5e-statblocks` | Create Fantasy Statblocks in Obsidian.md |
| [Fast Image Auto Uploader](https://github.com/eust-w/obsidian-image-auto-upload) | `fast-image-upload` | Uploads clipboard images using goPic |
| [Fast Text Color](https://github.com/Superschnizel/obsidian-fast-text-color) | `fast-text-color` | Quickly apply fully integrated text coloring and formatting with a custom syntax and a keyboard-centric interface. |
| [FastForwardLink](https://github.com/IdanLib/ObsidianFastForwardLinkPlugin) | `fast-forward-link` | Fast-forward multiple links to a single target note. Create custom link shorthands (like `ps` > `photoshop`) to create synonyms, streamline navigation, and keep your vault organized. |
| [Fastimer](https://github.com/vkostyanetsky/ObsidianFastimer) | `fastimer` | Intermittent fasting tracker. |
| [Favorite Note](https://github.com/mahmudz/obsidian-favorite-plugin) | `favorite-note` | Mark your note as favorite. |
| [Featured Image](https://github.com/johansan/obsidian-featured-image) | `featured-image` | Automatically sets a featured image property in your notes based on the first image, YouTube link, or Auto Card Link image found in your document. |
| [Feedly Annotations Sync](https://github.com/Fleker/feedly-for-obsidian) | `feedly-annotations` | Syncs Feedly highlights and annotations to a folder in your vault. |
| [Feeds](https://github.com/lukemt/obsidian-feeds) | `feeds` | Create feeds of topic-specific bullet points in Obsidian. |
| [Fetch Prayer Times](https://github.com/Eccys/obsidian-prayer-times) | `fetch-prayer-times` | Fetches local prayer times and saves them to a file. |
| [FFmpeg Converter](https://github.com/MrAnyx/obsidian-ffmpeg-converter) | `ffmpeg-converter` | Convert most used file formats into another format using FFmpeg and FFprobe to optimize your vault space |
| [Fight Note](https://github.com/Loac/obsidian-fight-note) | `fight-note` | Render Tekken notation into an easy-to-read format (partially useful for other fighting games: Guilty Gear, Street Fighter and etc). |
| [Figma Embed](https://github.com/kocheck/obsidian-figma-viewer) | `figma-embed` | Embed Figma files as inline previews. |
| [File Chucker](https://github.com/kenlim/file-chucker-plugin) | `file-chucker` | Quickly move a file to a new or existing folder, then open the next file. |
| [File Cleaner](https://github.com/johnsonhong997/obsidian-file-cleaner) | `obsidian-file-cleaner` | Help you to clean empty files and unused attachments in the vault. |
| [File Cleaner Redux](https://github.com/husjon/obsidian-file-cleaner-redux) | `file-cleaner-redux` | Help you to clean empty files and unused attachments in the vault. |
| [File Color](https://github.com/ecustic/obsidian-file-color) | `obsidian-file-color` | An Obsidian plugin for setting colors on folders and files in the file tree. |
| [File Compressor](https://github.com/networkmastered/obsidian-compress) | `compress` | Make your files smaller with compression! |
| [File Cooker](https://github.com/ivaneye/obsidian-files-cooker) | `obsidian-file-cooker` | Deal multi notes from Search results、current file、Dataview query string... |
| [File Creation and Last Modified Timestamps in Status Bar](https://github.com/Yustynn/obsidian-last-modified-timestamp-in-status-bar) | `last-modified-timestamp-in-status-bar` | Dynamic display of file modification and creation timestamps in the status bar. |
| [File Diff](https://github.com/friebetill/obsidian-file-diff) | `file-diff` | Shows the differences between two files.. |
| [File Explorer Markdown Titles](https://github.com/Dyldog/file-explorer-markdown-titles) | `file-explorer-markdown-titles` | Shows the first markdown header of a note in the file explorer |
| [File Explorer Note Count](https://github.com/ozntel/file-explorer-note-count) | `file-explorer-note-count` | The plugin helps you to see the number of notes under each folder within the file explorer. |
| [File Explorer++](https://github.com/kelszo/obsidian-file-explorer-plus) | `file-explorer-plus` | Hide and pin files and folders in the file explorer using custom filters, such as wildcards and regex, based on their names, paths, and tags. Additionally, achieve the same with a single click in the file menu. |
| [File Forgetting Curve](https://github.com/ptrsvltns/file-forgetting-curve-obsidian) | `file-forgetting-curve-obsidian` | File Forgetting Curve |
| [File Hider](https://github.com/Eldritch-Oliver/file-hider) | `OA-file-hider` | An Obsidian plugin that allows hiding files and folders in the built-in file explorer |
| [File Ignore](https://github.com/Feng6611/Obsidian-File-Ignore) | `file-ignore` | Control file indexing by adding or removing dot prefix to show or hide files, providing a .gitignore-like experience |
| [File Include](https://github.com/tillahoffmann/obsidian-file-include) | `file-include` | Include or embed files in Obsidian markdown. |
| [File Index](https://github.com/Steffo99/obsidian-file-index) | `file-index` | Create a metadata file about the files present in the Vault |
| [File indicators](https://github.com/JakobMick/obsidian-file-indicators) | `file-indicators` | Add custom indicators to the file explorer. |
| [File Info Panel](https://github.com/CattailNu/obsidian-file-info-panel-plugin) | `obsidian-file-info-plugin` | Plugin for Obsidian that creates a File Information view that displays the active file's date created, date modified, file size, and links to open the file in its native application and to open the file's folder.  It also has writing statistics (character, word, sentence, and paragraph counts) and a word frequency analysis. |
| [File Manager](https://github.com/jfsicilia/obsidian-file-manager) | `file-manager` | Adds missing features to the file explorer. |
| [File Order](https://github.com/lukasbach/obsidian-file-order) | `file-order` | Use number-prefixes in your file names to define a custom order, and drag-and-drop the files to update that order |
| [File path to URI](https://github.com/MichalBures/obsidian-file-path-to-uri) | `obsidian-file-path-to-uri` | Convert file path to uri for easier use of links to local files outside of Obsidian |
| [File Preview](https://github.com/xhuajin/obsidian-file-preview) | `file-preview` | Add file preview contents under file in file explorer. |
| [File Publisher](https://github.com/yiglas/obsidian-file-publisher) | `file-publisher` | Publishes a file to a given api. |
| [File Share](https://github.com/muckmuck96/obsidian-file-share) | `file-share` | Enables end-to-end encrypted file sharing directly between vaults via a socket server. |
| [File Title Updater](https://github.com/wenlzhang/obsidian-file-title-updater) | `file-title-updater` | Synchronize titles between filename, frontmatter, and first heading in notes. |
| [File Tree Alternative](https://github.com/ozntel/file-tree-alternative) | `file-tree-alternative` | This plugin allows you to have an alternative file tree view. |
| [File Tree Generator](https://github.com/Unarray/file-tree-generator) | `file-tree-generator` | Generate a file tree using Obsidian callouts. |
| [Filename Emoji Remover](https://github.com/YTolun/obsidian-filename-emoji-remover) | `obsidian-filename-emoji-remover` | This is a simple plugin to automatically remove emojis from filenames. Main purpose is to get rid of Dropbox sync issues for Readwise imported content. |
| [Filename Heading Sync](https://github.com/dvcrn/obsidian-filename-heading-sync) | `obsidian-filename-heading-sync` | Obsidian plugin for keeping the filename with the first heading of a file in sync |
| [FileName Styler](https://github.com/marc-f/obsidian-file-name-styler) | `filename-styler` | Customize and style file names in the file explorer using patterns, prefixes, suffixes, colors, and icons. |
| [Fill in the Blank (FITB)](https://github.com/mister-mcgee/obsidian-fill-in-the-blank) | `fill-in-the-blank` | Use --magic-- to render inline text as blank line(s) instead. |
| [Filtered Opener](https://github.com/Balibaloo/obsidian-filtered-opener) | `filtered-opener` | Open notes and folders. Chose from sets defined by filters. |
| [Financial Doc](https://github.com/studiowebux/obsidian-findoc) | `findoc` | Financial Documentation and Tracking using CSV format and Chart.js directly in Obsidian |
| [Find & Replace in Selection](https://github.com/TClark1011/obsidian-find-and-replace-in-selection) | `obsidian-find-and-replace-in-selection` | Replace text within your current selection. |
| [Find and replace in selection](https://github.com/dy-sh/obsidian-find-and-replace-in-selection) | `find-and-replace-in-selection` | Finds what you are looking for in the selected text and replaces it with the specified text |
| [Find orphaned files and broken links](https://github.com/Vinzent03/find-unlinked-files) | `find-unlinked-files` | Find files that are not linked anywhere and would otherwise be lost in your vault. In other words: files with no backlinks. |
| [Find Orphaned Images](https://github.com/josmarcristello/Obsidian-Find-Orphaned-Images) | `find-orphaned-images` | Finds images in the vault that are not linked to any notes. Either lists, or deletes them. |
| [Finnish Spellcheck](https://github.com/antoKeinanen/obsidian-finnish-spellcheck) | `finnish-spellcheck` | Spellchecker for the Finnish language using Voikko. / Oikolukija suomenkielellä, joka hyödyntää Voikkoa. |
| [Fit](https://github.com/joshuakto/fit) | `fit` | Minimalist File gIT (FIT) to sync your files across mobile and desktop devices using GitHub. |
| [Fix Line Endings on Copy](https://github.com/KiwiJanus/obsidian-line-ending-copyfix) | `line-ending-copyfix` | Change line endings to CRLF when copying text on Windows (add carriage return). |
| [Fix Math](https://github.com/loglux/fix-math-for-obsidian) | `fix-math` | Convert LaTeX equations from ChatGPT and AI assistants to Obsidian format: block equations to display math, inline to inline math. |
| [Flashcard Generator](https://github.com/chloedia/Obsidian_Quiz_Generator) | `flashcard-gen` | Craft insightful quizzes: Generate key questions/answers pairs from your notes effortlessly using Open ai's GPT-3/4 or local models. Elevate and optimize your learning journey. |
| [Flashcards](https://github.com/reuseman/flashcards-obsidian) | `flashcards-obsidian` | Anki integration |
| [Flashcards LLM](https://github.com/crybot/obsidian-flashcards-llm) | `flashcards-llm` | Use Large Language Models (such as ChatGPT) to automatically generate flashcards from obsidian notes |
| [Flexible Pomodoro For Obsidian](https://github.com/grassbl8d/flexible-pomo-obsidian) | `obsidian-flexible-pomo` | Adds a pomodoro timer to your status bar. This pomodoro has additional options such as early log and extend. |
| [Floating Headings](https://github.com/k0src/Floating-Headings-Obsidian-Plugin) | `floating-headings` | Displays a floating, collapsible outline of a note's headings on the right side of the editor. Expands on hover, click to navigate. |
| [Floating Highlights](https://github.com/KarthikRaju391/obsidian-float) | `floating-highlights` | Enhanced highlights for Obsidian |
| [Floating Search](https://github.com/Quorafind/Obsidian-Float-Search) | `float-search` | You can use search view in modal/leaf/popout window now. |
| [floating toc](https://github.com/PKM-er/obsidian-floating-toc-plugin) | `floating-toc` | This is a floating Toc plugin that  hovers a table of content  containing a header level on the notes sidebar. |
| [Floccus Bookmarks to Markdown](https://github.com/mddevils/floccus-bookmarks-to-markdown) | `floccus-bookmarks-to-markdown` | Bring your Bookmarks from Floccus to your Obsidian |
| [Flomo Importer](https://github.com/jia6y/flomo-to-obsidian) | `flomo-importer` | Make Flomo Memos to Obsidian Notes |
| [Flow](https://github.com/tavva/flow) | `flow` | Implements key processes in David Allen's Getting Things Done (GTD) methodology |
| [Flowcharts](https://github.com/land0r/obsidian-flowchart-plugin) | `flowcharts` | Render flowcharts using flowchart.js syntax. |
| [Focus Active Sentence](https://github.com/artisticat1/focus-active-sentence) | `focus-active-sentence` | Highlight the sentence the cursor is currently resting on. |
| [Focus and Highlight](https://github.com/nagi1999a/obsidian-focus-plugin) | `obsidian-focus-plugin` | A plugin for Obsidian (https://obsidian.md) that will highlight and focus on the currently selected heading |
| [Focus Mode](https://github.com/ryanpcmcquen/obsidian-focus-mode) | `obsidian-focus-mode` | Add Focus Mode to Obsidian. |
| [Focus Time](https://github.com/astradev123/obsidian-focus-time) | `focus-time` | Track the time spent on each note and visualize the data. |
| [Focus Tracker](https://github.com/jeetsukumaran/obsidian-focus-tracker) | `focus-tracker` | Track and align your focus. |
| [Fold Anywhere](https://github.com/Quorafind/Obsidian-Fold-Anywhere) | `fold-anywhere` | Set start and end marker, and then fold any text anywhere. |
| [Fold Properties](https://github.com/itsonlyjames/obsidian-fold-properties) | `fold-properties` | Adds fold/unfold properties function to folder context menu |
| [Fold Properties By Default](https://github.com/tbergeron/obsidian-fold-properties-by-default) | `fold-properties-by-default` | Always have editor/metadata properties folded by default. |
| [Folder by tags distributor](https://github.com/RevoTale/obsidian-folder-by-tags-distributor) | `folder-by-tags-distributor` | Automatically move notes into existing folders by tags specified in note. |
| [Folder Canvas](https://github.com/nancyel/obsidian-foldercanvas-plugin) | `foldercanvas` | Generate a Canvas view of your folder structure. |
| [Folder Filelist](https://github.com/band/obsidian-folder-filelist) | `folder-filelist` | Create and maintain a list of wikilinks to files in specified folders |
| [Folder Focus Mode](https://github.com/grochowski/obsidian-folder-focus-mode) | `obsidian-folder-focus-mode` | Focus file explorer on chosen folder and its files and subdirectories, while hiding all the other elements. |
| [Folder Index](https://github.com/turulix/obsidian-folder-index) | `obsidian-folder-index` | This Plugin will automatically generate a TOC for the current Folder. |
| [Folder Links](https://github.com/SteveOverSea/obsidian-folder-links) | `folder-links` | Clicking a link to a folder makes it revealed in the navigation. |
| [Folder Navigator](https://github.com/wenlzhang/obsidian-folder-navigator) | `folder-navigator` | Quickly navigate to folders in your vault using fuzzy search. |
| [Folder Note](https://github.com/xpgo/obsidian-folder-note-plugin) | `folder-note-plugin` | Click a folder node to show a note describing the folder. |
| [Folder notes](https://github.com/LostPaul/obsidian-folder-notes) | `folder-notes` | Create notes within folders that can be accessed without collapsing the folder, similar to the functionality offered in Notion. |
| [Folder overview](https://github.com/LostPaul/obsidian-folder-overview) | `folder-overview` | Provides a dynamic overview of your vault or folders in the format of a code block. |
| [Folder Periodic Notes](https://github.com/andrewheekin/obsidian-folder-periodic-notes) | `folder-periodic-notes` | Periodic notes in a year, month, and day folder hierarchy. |
| [Folder Tabulation](https://github.com/SpeedaRJ/obsidian_folder_tabulation) | `folder-tabulation` | Enables navigation between files in a folder via hotkeys and commands. |
| [FolderFile Splitter](https://github.com/XuQuan-nikkkki/FolderFile-Splitter-Plugin) | `folder-file-splitter` | Splits folder and file lists into separate views, simplifying navigation, improving clarity, and making it more intuitive to organize your notes. |
| [Folders to Graph](https://github.com/ratibus11/folders2graph) | `folders2graph` | Display your vault folder structure into your graphs. |
| [Font Size Adjuster](https://github.com/RyotaUshio/obsidian-font-size) | `font-size` | Adjust font size via commands. |
| [Fontsource](https://github.com/fontsource/obsidian-fontsource) | `fontsource` | Load custom fonts from Fontsource into your notes. |
| [Food Tracker](https://github.com/forketyfork/obsidian-food-tracker) | `food-tracker` | Track your food intake (calories, macronutrients) and nutritional information |
| [Foodiary](https://github.com/vkostyanetsky/ObsidianFoodiary) | `foodiary` | Food tracker, macronutrient and calorie calculator. |
| [Footlinks](https://github.com/DahaWong/obsidian-footlinks) | `footlinks` | Extracts links from the main text to footer. |
| [Footnote Shortcut](https://github.com/MichaBrugger/obsidian-footnotes) | `obsidian-footnotes` | Insert and write footnotes faster |
| [Force note view mode](https://github.com/bwydoogh/obsidian-force-view-mode-of-note) | `obsidian-view-mode-by-frontmatter` | This plugin allows to force the view mode and editing mode for a note by using front matter |
| [Force Read Mode](https://github.com/al3xw/force-read-mode) | `force-read-mode` | Forces Markdown files in specified folders to open in read-only mode. |
| [Format Automatically with Prettier](https://github.com/dylanarmstrong/obsidian-prettier-plugin) | `prettier-format` | Format files with Prettier using built-in settings for configuration. |
| [Format code](https://github.com/iVariable/Obsidian-Format-Code) | `obsidian-format-code` | This plugin introduces commands to format code (internally uses prettier) |
| [Format Hotkeys](https://github.com/anstosa/format-hotkeys-obsidian) | `format-hotkeys-obsidian` | Google Docs style formatting hotkeys for Obsidian |
| [Format with Prettier](https://github.com/alexgavrusev/obsidian-format-with-prettier) | `format-with-prettier` | Format files in your vault using Prettier. |
| [Formatto](https://github.com/evasquare/formatto) | `formatto-format` | Simple, fast, and easy-to-use Markdown formatter. |
| [Forms](https://github.com/sorinmircea/obsidian-forms-plugin) | `forms` | Publish beautiful forms and get responses straight to your vault. |
| [Fountain](https://github.com/bgrundmann/obsidian-fountain) | `fountain` | Write and view screenplays in Fountain format with index cards and lots of other features. |
| [Fountain Editor](https://github.com/chuangcaleb/obsidian-fountain-editor) | `fountain-editor` | Fountain (screenplay) syntax highlighting in the editor |
| [Freeform](https://github.com/tmcw/obsidian-freeform) | `freeform` | Make visualizations and run arbitrary code with JavaScript + iframe blocks. |
| [Friday](https://github.com/mdfriday/obsidian-friday-plugin) | `mdfriday` | Notes to Website. Friday helps you turn Markdown documents into websites in minutes. |
| [Friend Tracker](https://github.com/buzzguy/friend-tracker) | `friend-tracker` | Keep track of friends, birthdays, reminders, and interactions in Obsidian. Build a personal CRM, log connections, and stay organized inside your vault. |
| [From Template](https://github.com/mo-seph/obsidian-note-from-template) | `obsidian-notes-from-template` | Create new notes from Templates - for each Template, provides a Command to trigger it, and a form to fill in any variables in the template |
| [Front Matter Timestamps](https://github.com/pookhaosc1/obsidian-front-matter-timestamps) | `front-matter-timestamps` | Automatically manages and updates 'created' and 'modified' timestamps in the frontmatter of your notes |
| [Front Matter Title](https://github.com/snezhig/obsidian-front-matter-title) | `obsidian-front-matter-title-plugin` | Lets you define a title in frontmatter to be displayed as the filename for explorer, graph, search and etc. |
| [Frontmatter Alias Display](https://github.com/notmuhammad/obsidian-frontmatter-alias-display) | `frontmatter-alias-display` | A plugin for Obsidian to show front-matter aliases as display names in the File Explorer. |
| [Frontmatter generator](https://github.com/HananoshikaYomaru/Obsidian-Frontmatter-Generator) | `frontmatter-generator` | Generate frontmatter for your notes from json and javascript |
| [Frontmatter Markdown Links](https://github.com/mnaoumov/obsidian-frontmatter-markdown-links) | `frontmatter-markdown-links` | Adds support for markdown links in frontmatter |
| [Frontmatter Metadata Link Classes](https://github.com/zmeeeeeva/obsidian-plugin-metadata-link-classes) | `frontmatter-link-classes` | Adds classes to internal links based on frontmatter metadata. |
| [Frontmatter Tag Suggest](https://github.com/jmilldotdev/obsidian-frontmatter-tag-suggest) | `obsidian-frontmatter-tag-suggest` | Autocompletes tags in the frontmatter tags field |
| [Frontmatter to HTML Attributes](https://github.com/IllDepence/obsidian-frontmatter-to-html-attributes) | `frontmatter-to-html-attributes` | Makes YAML frontmatter available as data-* attributes in HTML, enabling metadata based CSS styling. |
| [Full Calendar](https://github.com/obsidian-community/obsidian-full-calendar) | `obsidian-full-calendar` | Obsidian integration with Full Calendar (fullcalendar.io) |
| [Full Screen Toggle](https://github.com/DonkeyPacific/obsidian-full-screen-cross-platform-plugin) | `full-screen-cross-platform` | Fullscreen focus across all platforms. It helps you get more display space when you focus on reading notes, especially on mobile devices. |
| [Fullscreen mode plugin](https://github.com/Razumihin/obsidian-fullscreen-plugin) | `obsidian-fullscreen-plugin` | This plugin allows viewing a single document in fullscreen focus mode |
| [Furigana](https://github.com/uonr/obsidian-furigana) | `obsidian-furigana` | Helper plugin for furigana and <ruby> |
| [Future Dates](https://github.com/slonoed/obsidian-future-dates) | `future-dates` | Show list of future dates in vault |
| [Fuzzy Chinese Pinyin](https://github.com/lazyloong/obsidian-fuzzy-chinese) | `fuzzy-chinese-pinyin` | Provide the function of fuzzy search using Chinese Pinyin. |
| [Fuzzy Note Creator](https://github.com/HaloGamer33/Obsidian-Fuzzy-Note-Creator) | `fuzzy-note-creator` | Create notes in folders with the help of a fuzzy finder. |
| [Game Search](https://github.com/CMorooney/obsidian-game-search-plugin) | `game-search` | Helps you find games and create notes. Optional Steam Library Sync |
| [Gamificate your PKM](https://github.com/saertna/obsidian-gamified-pkm) | `gamified-pkm` | Enhance your Personal Knowledge Management with gamification elements. Boost motivation and achieve growth as you engage with your PKM. |
| [Gamified Tasks](https://github.com/dromse/obsidian-gamified-tasks) | `grind-manager` | Gamify your task management with rewards system, craft your tasks by tags. |
| [Garble Text](https://github.com/kurakart/garble-text) | `garble-text` | Garbling text in Obsidian turns all content in the entire app (notes, sidebar, etc) into lines so you can take screenshots without exposing sensitive data. |
| [Gay Toolbar](https://github.com/ChasKane/gay-toolbar) | `gay-toolbar` | Colorful, customizable toolbar, designed for mobile. |
| [GChat Reminder](https://github.com/anil-e/obsidian_gchat_plugin) | `ghcat-reminder` | Sends notifications to Google Chat Webhook based on due dates in Obsidian tasks. |
| [GDScript Syntax Highlighting](https://github.com/RobTheFiveNine/obsidian-gdscript) | `gdscript-syntax-highlighting` | Add live GDScript syntax highlighting to code blocks. |
| [Gemini AI Assistant](https://github.com/Artel250/Obsidian-Gemini-Assistant) | `chat-with-bard` | Use Google Gemini directly in obsidian for free. |
| [Gemini Assistant](https://github.com/eatgrass/obsidian-gemini-assistant) | `gemini-assistant` | Your Gemini AI assistant |
| [Gemini Generator](https://github.com/BjarneRentz/obsidian-gemini-generator) | `gemini-generator` | Let Google Gemini generator your notes! |
| [Gemini Scribe](https://github.com/allenhutchison/obsidian-gemini) | `gemini-scribe` | Interact with Gemini and use your notes as context. |
| [Gemmy](https://github.com/ericaxu/gemmy) | `gemmy` | 2023 April Fool's plugin brought to you by Obsidian |
| [Gene 🧬](https://github.com/MatissJurevics/Gene-AI) | `gene-ai` | Gene is an ai assistant for your second brain. It makes it easier than ever to creaate, manage and modify your notes. Gene is a plugin for Obsidian.md |
| [Generate Hash](https://github.com/zigahertz/obsidian-hash) | `generate-hash` | Generates a cryptographically strong pseudorandom hash. |
| [Generate Timeline](https://github.com/Shanshuimei/obsidian-generate-timeline) | `generate-timeline` | Generate timelines from tag folder file or metadata automatically by any time properties. |
| [Generic Initiative Tracker](https://github.com/beaurancourt/obsidian-generic-initiative-tracker) | `generic-initiative-tracker` | TTRPG Generic Initiative Tracker for Obsidian.md |
| [Geocoding Properties](https://github.com/jose-elias-alvarez/obsidian-geocoding-properties) | `geocoding-properties` | Insert address / location data from geocoding APIs as Obsidian properties. |
| [Get Info](https://github.com/chetachiezikeuzor/Get-Info-Plugin) | `get-info-plugin` | A small menu that is tucked inside your status bar and shows helpful information for your chosen file 📄. |
| [Get Stock Information](https://github.com/mikejongbloet/obsidian-get-stock-information) | `get-stock-information` | This plugin takes a stock symbol and returns a callout block with the latest stock information. |
| [Geulo](https://github.com/zzunebye/obsidian-google-liked-video) | `geulo-youtube-liked-video` | Fetch and manage all the YouTube videos you've liked, search and sort them, summarize with LLM (AI) and add them to your daily note. |
| [GH Links Shortener](https://github.com/dbarnett/obsidian-gh-links-shortener) | `gh-links-shortener` | Modifies pasted GitHub links to use short GitHub ref text as the link title. |
| [Ghost Fade Focus](https://github.com/skipadu/obsidian-ghost-fade-focus) | `ghost-fade-focus` | Focused on the current line, others faded like a ghost! |
| [Ghost Text](https://github.com/lawrencefeng17/obsidian-hidden-hyperlinks) | `hidden-hyperlinks` | Hide text behind display text and copy on click. |
| [Giphy](https://github.com/LucJager/giphy-plugin) | `giphy` | Search and insert gifs in a note. |
| [Gist](https://github.com/linjunpop/obsidian-gist) | `obsidian-gist` | This is a plugin to display the GitHub Gist. |
| [Gistr](https://github.com/Aetherinox/obsidian-gistr) | `gistr` | Integrate Opengist and Github gists into your notes, allowing you to create, update, and share between your notes and gist services |
| [Git](https://github.com/Vinzent03/obsidian-git) | `obsidian-git` | Integrate Git version control with automatic backup and other advanced features. |
| [Git Changelog](https://github.com/shumadrid/obsidian-git-changelog) | `git-changelog` | Uses Git to display dynamic vault and file changelogs in the sidebar, useful for spotting data loss. |
| [Git File Explorer](https://github.com/MateusMolina/obsidian-git-file-explorer) | `git-file-explorer` | Add relevant git information to detected git repostitories in the file explorer. |
| [Git Integration](https://github.com/noradroid/obsidian-git-integration) | `git-integration` | Easily backup vault on a remote repository. |
| [Git Url](https://github.com/khuongduy354/obsidian-git-url) | `git-url` | Create a url to your file on your git remote repo |
| [GitHobs](https://github.com/GabAlpha/obsidian-githobs) | `githobs` | Use Obsidian as Github issue editor! |
| [GitHub Copilot](https://github.com/Pierrad/obsidian-github-copilot) | `github-copilot` | Implement GitHub Copilot services (suggestion and chat) in Obsidian |
| [GitHub Embeds](https://github.com/MrGVSV/obsidian-github-embeds) | `github-embeds` | Embed GitHub issues, PRs, and code snippets directly in Obsidian. |
| [GitHub Gitless Sync](https://github.com/silvanocerza/github-gitless-sync) | `github-gitless-sync` | Sync a GitHub repository with vaults on different platforms without requiring git installation |
| [GitHub Integration](https://github.com/kazhuravlev/obsidian-github) | `github` | Import your starred GitHub repositories and pull requests into notes with metadata |
| [GitHub Issue Augmentation](https://github.com/samprintz/obsidian-issue-augmentation-plugin) | `github-issue-augmentation` | Augments GitHub issue IDs |
| [Github Issues](https://github.com/LonoxX/obsidian-github-issues) | `github-issues` | Track GitHub Issues, Pull Requests, GitLab Issues and Merge Requests directly in your vault |
| [GitHub Link](https://github.com/nathonius/obsidian-github-link) | `github-link` | Enrich your notes with issue and pull request content from GitHub |
| [GitHub Stars](https://github.com/flyingnobita/obsidian-github-stars) | `github-stars` | Displays the number of stars for GitHub repositories mentioned in notes. |
| [GitHub Sync](https://github.com/kevinmkchin/Obsidian-GitHub-Sync) | `github-sync` | Sync vault to personal GitHub. |
| [GitHub Tasks](https://github.com/Epistemic-Technology/obsidian-github-tasks) | `github-tasks` | Sync issues and pull requests from your GitHub account to tasks. |
| [GitHub Tracker](https://github.com/schaier-io/obsidian-github-tracker-plugin) | `github-tracker` | Track GitHub issues and pull requests in your vault |
| [Gitlab Issues](https://github.com/benr77/obsidian-gitlab-issues) | `obsidian-gitlab-issues` | Import issues from Gitlab into Obsidian. |
| [Gitlab Wiki Exporter](https://github.com/jrabmer/obsidian-to-gitlab-wiki) | `gitlab-wiki-export` | Makes your entire vault Gitlab Wiki compatible and exports it to a specified location. |
| [Gladdis](https://github.com/AurelienStebe/Gladdis) | `gladdis` | Gladdis (Generative Language Artificial Dedicated & Diligent Intelligence System) - it's an AI chatbot. |
| [Glasp](https://github.com/glasp-co/obsidian-glasp-plugin) | `glasp` | Import your Glasp highlights and notes into your vault. |
| [Global Hotkeys](https://github.com/mjessome/obsidian-global-hotkeys) | `obsidian-global-hotkeys` | Add support for global hotkeys |
| [Global Markdown Encryption](https://github.com/shlemiel/globaloe) | `global-markdown-encrypt` | In-memory AES256-GCM Markdown Encryption |
| [Global Proxy](https://github.com/windingblack/obsidian-global-proxy) | `global-proxy` | Use network proxy throughout Obsidian according to the rules configured in this plugin. |
| [Global Search and Replace](https://github.com/MahmoudFawzyKhalil/obsidian-global-search-and-replace) | `global-search-and-replace` | Search and replace in all vault files |
| [GLSL Viewer](https://github.com/iY0Yi/obsidian_glslviewer) | `glsl-viewer` | Preview GLSL shaders. |
| [Gnome Terminal Loader](https://github.com/CheeseCake87/gnome-terminal-loader) | `gnome-terminal-loader` | Adds sidebar action icons to quickly open the Gnome Terminal or to have the Gnome Terminal run a Python module |
| [Go To Heading](https://github.com/oin/obsidian-gotoheading) | `oin-gotoheading` | Quickly navigate between headings |
| [Go to Line](https://github.com/phibr0/obsidian-go-to-line) | `obsidian-go-to-line` | This Plugin provides a go to Line Command |
| [Go Up](https://github.com/JinmuGo/obsidian-go-up) | `go-up` | Go to the pages that says 'up' property |
| [Goal Tracker](https://github.com/GizmoRay/obsidian-goal-tracker) | `goal-tracker` | Track your goals with a calendar view |
| [Goban SGF](https://github.com/StinsonZhao/obsidian-plugin-goban-sgf) | `goban-sgf` | Obsidian plugin for recording Go games (SGF format goban). |
| [GoBoard](https://github.com/dsokolov/goboard) | `goboard` | Render Go game diagrams from Markdown code blocks. |
| [GoLinks](https://github.com/xavdid/obsidian-golinks) | `obsidian-golinks` | This is a plugin for Obsidian that renders go/links as clickable links. |
| [Google Blogger](https://github.com/privet-kitty/obsidian-blogger) | `google-blogger` | Publish notes to Google Blogger. |
| [Google Calendar](https://github.com/YukiGasai/obsidian-google-calendar) | `google-calendar` | Interact with your Google Calendar from Inside Obsidian |
| [Google Calendar and Contacts Lookup](https://github.com/ntawileh/obsidian-google-lookup) | `obsidian-google-lookup` | Import contact and calendar event information from your Google account |
| [Google Calendar Importer](https://github.com/lexafaxine/GoogleCalendarImporter) | `google-calendar-importer` | A simple and light-weighted google calendar importer, allow injecting the events / tasks of a day automatically to your daily notes, or import it to anywhere with a command. |
| [Google Contacts](https://github.com/aleksejs1/obsidian-contact-sync-plugin) | `google-contacts` | Synchronize your Google contacts with separate contact-notes |
| [Google Drive Sync](https://github.com/RichardX366/Obsidian-Google-Drive) | `google-drive-sync` | Syncs a vault into Google Drive for cross-platform use (works for iOS). |
| [Google Keep Import](https://github.com/daledesilva/obsidian_google-keep-import) | `google-keep-import` | Imports Google Keep backup files and attachments. Can also be used to import other files. Use the official Obsidian Importer plugin instead unless you need additional customisation of character mapping or importing of extraneous files. |
| [Google Photos](https://github.com/alangrainger/obsidian-google-photos) | `google-photos` | Embed Google Photos images using the new Picker API (Legacy Library API features removed) |
| [Google Tasks](https://github.com/YukiGasai/obsidian-google-tasks) | `obsidian-google-tasks` | Interact with your Google Tasks from Inside Obsidian |
| [GPG Encrypt](https://github.com/lajg-dev/Obsidian-Plugin-GPG-Inline-Encrypt) | `gpg-encrypt` | Plugin to encrypt partial text or complete notes using GPG technology, it is compatible with security keys such as YubiKey or traditional GPG encryption methods |
| [gpgCrypt](https://github.com/tejado/obsidian-gpgCrypt) | `gpg-crypt` | Seamlessly encrypts your notes using GPG. Supports smartcards for enhanced security! Keep your information safe and accessible only to you. |
| [GPT Assistant](https://github.com/M7mdisk/obsidian-gpt) | `gpt-assistant` | Use a GPT-3 based model on your notes and get personalized answers from your knowledge base. |
| [GPT-3 Notes](https://github.com/micahke/obsidian-gpt3-notes) | `gpt3-notes` | Create a note using OpenAI's GPT-3 language model. |
| [GPT-LiteInquirer](https://github.com/ittuann/obsidian-gpt-liteinquirer-plugin) | `gpt-liteinquirer` | Experience OpenAI ChatGPT assistance directly within Obsidian, drafting content without interrupting your creative flow. |
| [Grandfather](https://github.com/noatpad/obsidian-grandfather) | `obsidian-grandfather` | A simple plugin to display the time and date on the status bar |
| [Granola Sync](https://github.com/tomelliot/obsidian-granola-sync) | `granola-sync` | Sync Granola notes to your vault. |
| [Graph Analysis](https://github.com/SkepticMystic/graph-analysis) | `graph-analysis` | Analyse your Obsidian graph. |
| [Graph Banner](https://github.com/ras0q/obsidian-graph-banner) | `graph-banner` | Display a local graph view to the note header |
| [Graph Link Types](https://github.com/natefrisch01/Graph-Link-Types) | `graph-link-types` | Link types for graph view. |
| [Graphic Organizer](https://github.com/nickfreedom/obsidian-graphic-organizer) | `graphic-organizer` | Interactive tree view for visualizing and managing your vault's file hierarchy. |
| [Graphs](https://github.com/DylanHojnoski/obsidian-graphs) | `graphs` | Create interactive graphs by writing YAML |
| [Grappling Hook](https://github.com/chrisgrieser/grappling-hook) | `grappling-hook` | Obsidian Plugin for blazingly fast file switching. For those who find the Quick Switcher still too slow. |
| [GridExplorer](https://github.com/Devon22/obsidian-gridexplorer) | `gridexplorer` | Browse note files in a grid view. |
| [Group Snippets](https://github.com/Mara-Li/obsidian-group-snippets) | `obsidian-group-snippets` | Create folder of snippets to activate them in one click ! |
| [GTD No Next Step](https://github.com/saibotsivad/obsidian-gtd-no-next-step) | `gtd-no-next-step` | Adds a badge to Getting Things Done (GTD) "project" files with no defined next step. |
| [GTP Preview](https://github.com/Barba828/obsidian-plugin-gtp-preview) | `gtp-preview` | Supports rendering of GuitarPro files such as `gtp/gp/gp5/gpx`. |
| [Guid Renamer](https://github.com/taskscape/ObsidianUniqueFileName) | `guid-renamer` | Rename selected file with a random GUID. |
| [Guitar Chord](https://github.com/Barba828/obsidian-plugin-chord) | `guitar-chord` | Quickly enter and display guitar chords, with optional chords based on music theory. No need to write in code blocks, they can be inserted and edited directly in the document. |
| [Gyazo Viewer](https://github.com/nota/gyazo-obsidian-plugin) | `gyazo` | Display your Gyazo captures and embed them into your notes. |
| [Habit Calendar](https://github.com/hedonihilist/obsidian-habit-calendar) | `habit-calendar` | Monthly Habit Calendar for DataviewJS. This plugin helps you render a calendar inside DataviewJS code block, showing your habit status within a month. |
| [Habit Tracker](https://github.com/Narsail/habit-tracker-obsidian) | `habit-tracker` | Track your Habits. |
| [Habit Tracker](https://github.com/duoani/obsidian-habit-tracker) | `obsidian-habit-tracker` | This plguin creates a simple Month view for visualizing your punch records. |
| [Habit Tracker 21](https://github.com/zincplusplus/habit-tracker) | `habit-tracker-21` | Your 21-day journey to habit formation, simplified |
| [Habitica Sync](https://github.com/SuperChamp234/habitica-sync) | `obsidian-habitica-integration` | This plugin helps integrate Habitica user tasks and stats into Obsidian |
| [HackerNews](https://github.com/arpitbbhayani/obsidian-hackernews) | `obsidian-hackernews` | Periodically fetches and displays top stories from HackerNews. |
| [HackerOne](https://github.com/Neolex-Security/obsidian-hackerone) | `hackerone` | Unofficial plugin to fetch your bug reports from HackerOne. (needs dataview plugin) |
| [HackMD Sync](https://github.com/thor314/hackmd-obsidian) | `hackmd-sync` | An interface to upload notes to and from HackMD |
| [Hadith Lookup](https://github.com/iadnanmukhtar/obsidian-hadith-lookup-plugin) | `hadith-lookup` | Inserts Hadith and Quranic ayat and passages using a reference ID from the Ḥadīth Unlocked API (https://hadithunlocked.com) |
| [Halo](https://github.com/halo-sigs/obsidian-halo) | `halo` | Halo's Obsidian integration supports publishing content to Halo sites |
| [HamsterBase Official](https://github.com/hamsterbase/obsidian-hamsterbase) | `hamsterbase` | Official HamsterBase -> Obsidian integration |
| [Handlebars Dynamic Templating](https://github.com/hided62/obsidian-handlebars-dynamic) | `handlebars-dynamic` | Handlebars dynamic templating. Define template files and use them dynamically via hb blocks. Template recursion is also possible. |
| [Handlebars Template Plugin](https://github.com/sbquinlan/obsidian-handlebars) | `obsidian-handlebars` | This is a plugin for Obsidian that adds support for handlebars template blocks in notes. |
| [Handwriting OCR](https://github.com/ikmolbo/handwriting-ocr-obsidian-plugin) | `handwriting-ocr` | Transform handwritten documents and scanned images into editable text with Handwriting OCR's AI-powered handwriting to text conversion. |
| [Handwritten Notes](https://github.com/FBarrca/obsidian-handwritten-notes) | `handwritten-notes` | Annotate PDFs and create handwritten notes inside your vault using a stylus. |
| [Hanko](https://github.com/Telehakke/hanko) | `hanko` | Register and paste any text. |
| [Hanzi Writer](https://github.com/pakrentos/hanzi-writer-obsidian) | `hanzi-writer` | Interactive Chinese character writing blocks using Hanzi Writer |
| [Hard Breaks](https://github.com/bkis/obsidian-hard-breaks) | `hard-breaks` | Turn soft line breaks in Markdown into hard line breaks |
| [Hardcover](https://github.com/aliceinwaterdeep/obsidian-hardcover) | `hardcover` | Sync your Hardcover library to your notes. |
| [Harper](https://github.com/Automattic/harper-obsidian-plugin) | `harper` | The Grammar Checker for Developers |
| [Harpoon](https://github.com/rodrez/obsidian-harpoon) | `harpoon` | Use shortcuts to manage and navigate your top four frequently-used files in Obsidian. |
| [Hash Pasted Image](https://github.com/hardingadonis/hash-pasted-image) | `hash-pasted-image` | Auto rename pasted images added to the vault via hash algorithm SHA-512 |
| [Hatena Blog Publisher](https://github.com/takmatsukawa/obsidian-hatena) | `hatena` | Publish your Obsidian notes directly to Hatena Blog |
| [Header Adjuster](https://github.com/Netajam/header-adjuster) | `header-adjuster` | Easily adjust header levels in Markdown documents by increasing or decreasing their levels. Supports full document adjustments or specified line ranges, with default settings and commands for convenience |
| [Header Counter](https://github.com/nancyel/header-counter) | `header-counter` | Count the number of headers in the current note |
| [Header Enhancer](https://github.com/HoBeedzc/obsidian-header-enhancer-plugin) | `header-enhancer` | Level up your headers, customize your notes. Header Enhancer makes your notes header better and more useful. |
| [Header navigation](https://github.com/talwrii/obsidian-header-navigation) | `header-navigation` | Various functions to navigate between headers. |
| [Heading Decorator](https://github.com/dragonish/obsidian-heading-decorator) | `heading-decorator` | Implement displaying specific content around headings based on their levels. |
| [Heading Helper](https://github.com/sidkhuntia/obsdian-headings-helper) | `heading-helper` | Cycle heading levels and display visual heading indicators in the gutter |
| [Heading Level Indent](https://github.com/svonjoi/obsidian-heading-level-indent) | `heading-level-indent` | Indenting content under headers based on their level |
| [Heading Shifter](https://github.com/k4a-l/obsidian-heading-shifter) | `obsidian-heading-shifter` | Easily Shift and Change markdown headings. |
| [Heading Toggler](https://github.com/Lord-Turmoil/heading-toggler-obsidian) | `heading-toggler` | Easily toggle heading levels in Markdown documents with shortcuts. |
| [Headings in Explorer](https://github.com/patrickchiang/obsidian-headings-in-explorer) | `headings-in-explorer` | Show headings in the file explorer. |
| [Heatmap Calendar](https://github.com/Richardsl/heatmap-calendar-obsidian) | `heatmap-calendar` | Activity Year Overview for DataviewJS, Github style – Track Goals, Progress, Habits, Tasks, Exercise, Finances, "Dont Break the Chain" etc. |
| [Heatmap Tracker](https://github.com/mokkiebear/heatmap-tracker) | `heatmap-tracker` | Visualize your activity and track goals, progress, habits, tasks, exercise, finances, and more—all in a single, interactive heatmap! |
| [hello nemesis](https://github.com/adiguno/hello-nemesis) | `hello-nemesis` | Uses OpenAI to challenge your ideas. |
| [HelpMate](https://github.com/TfTHacker/obsidian42-HelpMate) | `helpmate` | Integrating help systems into the Obsidian UI. |
| [Hephaistos Importer](https://github.com/runa-rist/hephaistos-importer) | `hephaistos-importer` | Imports main stats from the Starfinder RPG character website Hephaistos. |
| [heti](https://github.com/moeyua/obsidian-heti) | `heti` | 赫蹏（hètí）是专为中文内容展示设计的排版样式增强。它基于通行的中文排版规范而来，可以为网站的读者带来更好的文章阅读体验。 |
| [Hexo Publisher](https://github.com/zhenlohuang/obsidian-hexo-publisher) | `hexo-publisher` | Publish your notes to Hexo |
| [Hexo Toolkit](https://github.com/sissilab/obsidian-hexo-toolkit) | `hexo-toolkit` | Maintain Hexo posts. |
| [Hidden Folder](https://github.com/ptrsvltns/hidden-folder-obsidian) | `hidden-folder-obsidian` | Hidden Folder |
| [Hide Commands in Menu](https://github.com/bomian98/obsidian-hide-commands-in-menu) | `hide-commands-in-menu` | Allows you to hide any command to different menu. |
| [Hide Folders](https://github.com/JonasDoesThings/obsidian-hide-folders) | `hide-folders` | Hides & Toggles configured folders (e.g. attachments folders). |
| [Hide Index Files](https://github.com/d7sd6u/obsidian-hide-index-files) | `hide-index-files` | Hide index files (folder notes) more reliably. |
| [Hide Sidebars on Window Resize](https://github.com/NomarCub/obsidian-hide-sidebars-on-window-resize) | `obsidian-hide-sidebars-when-narrow` | Automatically hides the sidebars when your window is resized to be narrower |
| [Hider](https://github.com/kepano/obsidian-hider) | `obsidian-hider` | Hide UI elements such as tooltips, status, titlebar and more |
| [Hierarchical Backlinks](https://github.com/jasonmotylinski/hierarchical-backlinks) | `hierarchical-backlinks` | Displays backlinks in a hierarchy |
| [Hierarchical Outgoing Links](https://github.com/jasonmotylinski/hierarchical-outgoing-links) | `hierarchical-outgoing-links` | Displays outgoing links in a hierarchy |
| [Hierarchy](https://github.com/kdnk/obsidian-hierarchy) | `hierarchy` | Display the hierarchy instead of just the file name. |
| [Highlight active folder section](https://github.com/justanotherjurastudent/highlight-active-folder-section) | `highlight-active-folder-section` | Highlight the active folder section and the title in the file explorer. |
| [Highlight Helper](https://github.com/byfun/obsidian-highlight-helper) | `highlight-helper` | Helper to copy and paste highlights |
| [Highlight Public Notes](https://github.com/dennisseidel/highlightpublicnotes-obsidian-plugin) | `obsidian-highlightpublicnotes-plugin` | This plugin warns that a note is public (based on a frontmatter attribute) by colorizing the note red. |
| [Highlightr](https://github.com/chetachiezikeuzor/Highlightr-Plugin) | `highlightr-plugin` | A minimal and aesthetically pleasing highlighting menu that makes color-coded highlighting much easier with a configurable assortment of highlight colors 🎨. |
| [Hill Charts](https://github.com/stufro/obsidian-hill-charts) | `hill-charts` | Add Hill Charts to your notes. |
| [HiNote](https://github.com/CatMuse/HiNote) | `hi-note` | Add comments to highlighted notes, use AI for thinking, and flashcards for memory. |
| [Hints Flow](https://github.com/slpbx/obsidian-plugin) | `hints-plugin` | Save data directly to Obsidian with a specified template. Capture from Telegram, WhatsApp, Slack, Email, SMS, Raycast and more. |
| [historica](https://github.com/nhannht/obsidian-historica) | `historica` | Intelligently generates timeline from your content ... like a bro! |
| [History Today](https://github.com/Yaob1990/obsidian-history-today) | `history-today` | View and review your historical notes from this day across previous years |
| [HiWords](https://github.com/CatMuse/HiWords) | `hi-words` | Effortlessly grow your vocabulary as you read, with automatic highlighting and translation of unfamiliar words. |
| [HK Code Block](https://github.com/HeekangPark/obsidian-hk-code-block) | `hk-code-block` | Obsidian plugin developed by Heekang Park; Make code block looking good on reading view |
| [Hledger Notes](https://github.com/bzimor/obsidian_hledger) | `hledger-notes` | Create and manage hledger entries directly in your vault. |
| [Hoarder Sync](https://github.com/jhofker/obsidian-hoarder) | `hoarder-sync` | Sync your Hoarder bookmarks |
| [HOME key](https://github.com/shichishima/obsidian-homekey-plugin) | `homekey-action` | Move cursor to beginning of text, considering Markdown heading characters. |
| [Home tab](https://github.com/olrenso/obsidian-home-tab) | `home-tab` | A browser-like search tab for your local files. |
| [Homepage](https://github.com/mirnovov/obsidian-homepage) | `homepage` | Open a specified note, canvas, base, or workspace on startup, or set it for quick access later. |
| [Homework Manager](https://github.com/kadisonm/obsidian-homework-plugin) | `homework-manager` | Keeps track of homework through a to-do list. |
| [Horizontal Blocks](https://github.com/iCodeAlchemy/horizontal-blocks) | `horizontal-blocks` | Notion-style resizable side-by-side Markdown blocks that support text, images, embeds, and internal links. |
| [Hotkey Helper](https://github.com/pjeby/hotkey-helper) | `hotkey-helper` | Easily see and access any plugin's settings or hotkey assignments (and conflicts) from the Community Plugins tab |
| [Hotkeys Chords](https://github.com/trenta3/obsidian-hotkeys-chords) | `obsidian-hotkeys-chords` | Set hotkeys chords to activate commands |
| [Hotkeys for Bookmarks](https://github.com/Vinzent03/obsidian-shortcuts-for-starred-files) | `obsidian-shortcuts-for-starred-files` | Set an individual hotkey for the first 9 bookmarks and open them just with your keyboard. |
| [Hotkeys for specific files](https://github.com/Vinzent03/obsidian-hotkeys-for-specific-files) | `obsidian-hotkeys-for-specific-files` | Set hotkeys for specific files and open them just with your keyboard. |
| [Hotkeys for templates](https://github.com/Vinzent03/obsidian-hotkeys-for-templates) | `obsidian-hotkeys-for-templates` | Add hotkeys to insert specific templates |
| [Hotkeys++](https://github.com/argenos/hotkeysplus-obsidian) | `hotkeysplus-obsidian` | Additional hotkeys to do common things in Obsidian |
| [Hotstrings](https://github.com/wakywayne/obsidian-hotstrings) | `hotstrings` | Set custom hotstrings that get expanded to text once typed. |
| [Hover Editor](https://github.com/nothingislost/obsidian-hover-editor) | `obsidian-hover-editor` | Transform the Page Preview hover popover into a fully working editor instance |
| [Hover External Link Plugin](https://github.com/jamiebrynes7/obsidian-hover-external-link) | `hover-external-link` | Hover on external links to see the destination URL. |
| [Hover Reveal](https://github.com/Asrieal/HoverReveal) | `hover-reveal` | Shows hidden text in tooltips when hovering over marked elements using [visibleText]{tooltipText} syntax. Supports custom hotkeys. |
| [HTML checkboxes](https://github.com/anareaty/html-checkboxes) | `html-checkboxes` | Allows to quickly add HTML checkboxes to your notes and makes them clickable. |
| [HTML Reader](https://github.com/nuthrash/obsidian-html-plugin) | `obsidian-html-plugin` | This is a HTML file reader plugin for Obsidian. Can open document with ".html" and ".htm" file extensions. |
| [Html Server](https://github.com/Pr0dt0s/obsidian-html-server) | `html-server` | This plugin lets you spin up a local http server to access your vault via a web browser from any device in your network. |
| [HTML Tabs](https://github.com/ptournet/obsidian-html-tabs) | `html-tabs` | Create and render Tabs and tab panels in your notes. |
| [HTML Tags Autocomplete](https://github.com/bicarlsen/obsidian_html_tags_autocomplete) | `obsidian-html-tags-autocomplete` | Autocomplete HTML tags. |
| [HTTP Link Maker](https://github.com/kennethac/obsidian-http-links-plugin) | `http-link-maker` | Copies an HTTP link that will redirect to your vault but will be recognized and work across browsers and programs |
| [Hugo codeblock highlight](https://github.com/aarol/obsidian-hugo-codeblock-highlight) | `hugo-codeblock-highlight` | Highlights lines in codeblocks using Hugo's hl_lines syntax. |
| [Hugo preview](https://github.com/fzdwx/hugo-preview-obsidian) | `hugo-preview-obsidian` | Hugo preview in obsidian |
| [Hugo Publish](https://github.com/kirito41dd/obsidian-hugo-publish) | `hugo-publish` | Publish your blog to hugo site. |
| [Hunchly](https://github.com/shadowoption/Hunchly-obsidian-plugin) | `hunchly` | This plugin converts an Hunchly case into Obsidian notes enriching the data along the way. |
| [Hydrate](https://github.com/hydrateagent/hydrate) | `hydrate` | Cursor-like note agent with MCP support. |
| [Hyphenation](https://github.com/7596ff/obsidian-hyphenation) | `obsidian-hyphenation` | Enables justified text and hyphenation |
| [Hypothes.is](https://github.com/weichenw/obsidian-hypothesis-plugin) | `obsidian-hypothesis-plugin` | Sync your Hypothesis highlights |
| [Hârn Weather Generator](https://github.com/marcueberall/obsidian-harn-weather) | `harn-weather` | Unofficial Hârn weather generator. Generates the campaign weather for different time spans. The weather includes precipitation, temperature, wind direction and speed, moon phases and critical conditions for the whole of Western Venârivè. |
| [ibook](https://github.com/bingryan/obsidian-ibook-plugin) | `ibook` | plugin for apple ibook. |
| [iCal](https://github.com/andrewbrereton/obsidian-to-ical-plugin) | `ical` | Scans your vault for tasks. Creates an iCal file and stores it on Gist. You can then show this calendar in any iCal compatible client such as Outlook, Google Calendar, Apple Calendar, etc. |
| [iCloud Contacts](https://github.com/Trulsaa/obsidian-icloud-contacts) | `icloud-contacts` | Imports contacts from iCloud and manages a note for each contact. |
| [Icon Shortcodes](https://github.com/aidenlx/obsidian-icon-shortcodes) | `obsidian-icon-shortcodes` | Insert emoji and custom icons with shortcodes |
| [Icon Swapper](https://github.com/mgmeyers/obsidian-icon-swapper) | `obsidian-icon-swapper` | Allows swapping out Obsidian's default icons. |
| [Iconic](https://github.com/gfxholo/iconic) | `iconic` | Customize your icons and their colors directly from the UI, including tabs, files & folders, bookmarks, tags, properties, and ribbon commands. |
| [Iconize](https://github.com/FlorianWoelki/obsidian-iconize) | `obsidian-icon-folder` | Add icons to anything you desire in Obsidian, including files, folders, and text. |
| [Iconoir Icons](https://github.com/gapmiss/iconoir-icons) | `iconoir-icons` | Create & display customized SVG Iconoir icons. |
| [Icons](https://github.com/visini/obsidian-icons-plugin) | `obsidian-icons-plugin` | Add icons to your Obsidian notes. |
| [ICS](https://github.com/open-horizon-labs/obsidian-ics) | `ics` | Parse multiple ICS files to include in your notes. Designed for Daily Notes and the Day Planner format. Through templates you can customize it for other use cases. |
| [Idealogs Annotator](https://github.com/idlgcl/obsidialogs) | `idealogs-annotator` | For viewing, linking and annotating Idealogs articles. |
| [Idle Monitor](https://github.com/alberto98fx/idle-monitor-obsidian) | `idle-monitor` | Get notified when you stop typing to stay motivated. |
| [iDoRecall](https://github.com/iDoRecall/idorecall) | `idorecall` | iDoRecall plugin allows you to create recalls from Obsidian notes |
| [Ignore Filters Boost](https://github.com/Lavton/obsidian-ignore-filter-shortcut) | `ignore-filters-boost` | Update excluded files from the file explorer. |
| [ii](https://github.com/wish5115/obsidian-ii-quicker) | `ii-quicker` | Quickly insert common Markdown code and HTML code, and customize your own insertion commands. |
| [Image auto upload](https://github.com/renmu123/obsidian-image-auto-upload-plugin) | `obsidian-image-auto-upload-plugin` | This plugin uploads images from your clipboard by PicGo |
| [Image Border Style](https://github.com/shenoy-anurag/obsidian-image-border-style) | `image-border-style` | Border styling for images in markdown notes. |
| [Image Caption](https://github.com/bicarlsen/obsidian_image_caption) | `obsidian-image-caption` | Add captions to images. |
| [Image Captions](https://github.com/alangrainger/obsidian-image-captions) | `image-captions` | Adds captions to images when there is alt-text specified |
| [Image Classify Paste](https://github.com/ostoe/Ob-ImagePastePlugin) | `image-classify-paste` | paste your image like typora, the image link name not `![[Paste xxx]]` but `![some name](relative-directory/xxx.png)`with a relative directory. 类比于typora的方式粘贴图片到本地，存放在以当前md文档命名的文件夹里。 |
| [Image Collector](https://github.com/tdaykin/obsidian_image_collector) | `image_collector` | Collects all of the images in an Obsidian (markdown) note and exports them to a folder called 'file_name images'. |
| [Image Context Menus](https://github.com/NomarCub/obsidian-copy-url-in-preview) | `copy-url-in-preview` | Copy to clipboard, Copy URL, Open in default app, Show in system explorer, Reveal file in navigation, Open in new tab, Rename context menus for images. |
| [Image Converter](https://github.com/xRyul/obsidian-image-converter) | `image-converter` | Convert, compress, resize, annotate, markup, draw, crop, rotate, flip, align images directly in Obsidian. Drag-resize, rename with variables, batch process. WEBP, JPG, PNG, HEIC, TIF. |
| [Image Darkmodifier](https://github.com/0qln/obsidian-image-darkmodifier) | `image-darkmodifier` | Turn your inline images into darkmode (...and more!). |
| [Image Embedder](https://github.com/sky150/obsidian-image-embedder) | `image-embedder` | Automatically downloads and embeds images from URLs when pasting |
| [Image Gallery](https://github.com/lucaorio/obsidian-image-gallery) | `obsidian-image-gallery` | A zero setup masonry image gallery for Obsidian |
| [Image Helper](https://github.com/byfun/obsidian-image-helper) | `image-helper` | Context menu to convert a image to another format in reading view |
| [Image in Editor](https://github.com/ozntel/oz-image-in-editor-obsidian) | `oz-image-plugin` | View Images, Transclusions, iFrames and PDF Files within the Editor without a necessity to switch to Preview. |
| [Image Inline](https://github.com/ZackaryW/obsidian-image-inline) | `image-inline` | Paste your image without attachment files |
| [Image Inserter](https://github.com/cloudy9101/obsidian-image-inserter) | `insert-unsplash-image` | This plugin helps users easily search and insert images to editors from Unsplash / Pixabay / Pexels. |
| [Image Layouts](https://github.com/vertis/obsidian-image-layouts) | `obsidian-image-layouts` | Add beautiful image layouts to your notes |
| [Image Magician](https://github.com/luxmargos/obsidian-image-magician-plugin) | `image-magician` | Supports viewing and exporting various image formats powerd by ImageMagick. |
| [Image Metadata](https://github.com/alexeiskachykhin/obsidian-image-metadata-plugin) | `image-metadata` | Annotate photos with Exif and other metadata right from the image viewer screen. |
| [Image OCR](https://github.com/kaffarell/obsidian-tesseract-ocr) | `image-ocr` | Runs OCR on images and copies content in image caption. |
| [Image Picker](https://github.com/ariamckinley/obsidian-image-picker) | `image-picker` | Adds a UI panel for quickly selecting images that are in your vault. |
| [Image Preview on Icon Hover](https://github.com/rama1997/Image-Preview-On-Icon-Hover) | `image-preview-on-icon-hover` | Adds custom image previews when hovering over various UI icons. |
| [Image Search](https://github.com/razeghi71/obsidian-image-search) | `image-search` | Search and insert images using Brave Search API |
| [Image Share](https://github.com/iqijun/obsidian-image-share) | `image-share` | Share selected text as beautiful images |
| [Image Size](https://github.com/cynicalight/obsidian-image-size) | `image-size` | Set the default size for pasted images. |
| [Image to HTML](https://github.com/0x1DA9430/img2html) | `img2html` | Paste images as HTML format instead of wikilink or markdown format |
| [Image To Lskypro](https://github.com/NekoTarou/lskypro-auto-upload) | `lskypro-auto-upload` | Auto upload images from clipboard to lskypro |
| [Image to notes by Photes.IO](https://github.com/Kanaries/photes-io-obsidian-plugin) | `image-notes-photes-io` | Turn your images into text notes with AI |
| [Image to text OCR](https://github.com/dario-baumberger/obsidian-image-to-text-ocr) | `image-to-text-ocr` | Convert a image in your note to text. |
| [Image Toolkit](https://github.com/obsidian-community/obsidian-image-toolkit) | `obsidian-image-toolkit` | This plugin provides some image toolkit. |
| [Image Tools](https://github.com/Hosstell/image-tools-obsidian-plugin) | `image-tools` | Formatter for image on page |
| [Image Upload Toolkit](https://github.com/addozhang/obsidian-image-upload-toolkit) | `image-upload-toolkit` | Upload local images to remote store (Imgur, Gyazo, AliYun OSS, Imagekit, Amazon S3, TencentCloud COS, Qiniu Kodo, GitHub, Cloudflare R2 and Backblaze B2). |
| [Image Uploader](https://github.com/Creling/obsidian-image-uploader) | `obsidian-image-uploader` | This plugin uploads the image in your clipboard to any image hosting automatically when pasting. |
| [Image Uploader For Note](https://github.com/yy4382/obsidian-image-upload) | `image-uploader-for-note` | Upload images in a note, and remove the images from the vault if they're exclusively used within that note. |
| [Image Zoom & Drag](https://github.com/Ssentiago/image-zoom-drag) | `diagram-zoom-drag` | Make any image or diagram interactive with zoom, drag, and control panels |
| [Image2LaTEX](https://github.com/Hugo-Persson/obsidian-ocrlatex) | `image2latex` | Convert your images to Markdown and MathJax |
| [Images to Notes](https://github.com/rodolfo-terriquez/images-to-notes) | `images-to-notes` | Turn photos of handwritten or printed notes into Markdown using AI. |
| [IMDb](https://github.com/aaachen/IMDb-Obsidian) | `imdb-sync` | Sync your IMDb list |
| [ImgBB Uploader](https://github.com/jordanhandy/obsidian-imgbb-uploader) | `imgbb-uploader` | Upload images from your clipboard to ImgBB. |
| [Imgur](https://github.com/gavvvr/obsidian-imgur-plugin) | `obsidian-imgur-plugin` | This plugin uploads images from your clipboard to imgur.com and embeds uploaded image to your note |
| [Immersive Translate](https://github.com/imfenghuang/obsidian-immersive-translate) | `immersive-translate` | A free-to-use translatation service for foreign language markdown file. |
| [Immich](https://github.com/Talal-A/obsidian-immich) | `immich` | Link your Immich images within your vault. |
| [Import Attachments+](https://github.com/alberti42/obsidian-import-attachments-plus) | `import-attachments-plus` | Move and link the attachments into the vault. |
| [Import GitHub Readme](https://github.com/chasebank87/import-github-readme) | `import-github-readme` | Fetches and integrates GitHub README files into personal notesmai |
| [Import Todoist to Obsidian Tasks](https://github.com/dukex/obsidian-import-todoist) | `import-todoist` | Import Todoist tasks as Obsidian tasks. |
| [Import/Export TiddlyWiki](https://github.com/lucasbordeau/obsidian-tiddlywiki) | `tiddlywiki-import-export` | Import and export TiddlyWiki from and to Obsidian. |
| [Importer](https://github.com/obsidianmd/obsidian-importer) | `obsidian-importer` | Import data from Notion, Evernote, Apple Notes, Microsoft OneNote, Google Keep, Bear, Roam, Textbundle, CSV, and HTML files. |
| [Improved Random Note](https://github.com/ShockThunder/improved-random-note) | `improved-random-note` | Improved interaction with the knowledge base in so-called wandering mode by opening specific Random Notes. |
| [IMSwitch in Math Block](https://github.com/cailurus/imswitch_mathblock_obsidian) | `imswitch-mathblock` | Automatically switch input method in math block |
| [Inbox](https://github.com/Zachatoo/obsidian-inbox) | `inbox` | Show in app notification if there is data to process in the "inbox" note. |
| [Inbox Organiser](https://github.com/jamiefdhurst/obsidian-inbox-organiser) | `inbox-organiser` | Capture any new notes into an inbox and periodically prompt to organise these into other folders within the vault. |
| [Inboxer](https://github.com/eoinhurrell/obsidian-inboxer) | `inboxer` | Adds commands to quickly add entries to INBOX and TIMELINE sections |
| [Incomplete files](https://github.com/HananoshikaYomaru/obsidian-incomplete-files) | `incomplete-files` | Rule based keep track of your incomplete files |
| [Incremental ID](https://github.com/adziok/obsidian-incremental-id) | `incremental-id` | Allow to generate Jira like ids. |
| [Incremental Writing](https://github.com/bjsi/incremental-writing) | `obsidian-incremental-writing` | Incrementally review notes and blocks over time. |
| [Index Checker](https://github.com/pavloDeshko/obsidian-index-checker) | `index-checker` | Make sure your index "MOC" files (notes or Canvas) contain all links they should contain. |
| [Index Notes](https://github.com/adanielnoel/obsidian-index-notes) | `index-notes` | Keep your notes indexed based on their (hierarchical) tags |
| [Influx](https://github.com/jensmtg/influx) | `influx` | Transform your Obsidian backlinks from simple links into rich, contextual excerpts. See the actual content surrounding each link, turning your note connections into genuine insights. |
| [InfoFlow](https://github.com/InfoFlow/Obsidian-InfoFlow) | `infoflow` | Import your contents from InfoFlow to Obsidian. Similar to ReadWise or Omnivore importers. |
| [Infostacker Note Publish](https://github.com/taskscape/InfostackerPlugin) | `infostacker` | Easily share your notes, images and attachments publicly using private links |
| [InfraNodus AI Graph View](https://github.com/noduslabs/infranodus-obsidian-plugin) | `infranodus-graph-view` | Interactive 3D graph view: text analysis, topic modeling, gap detection, and AI. |
| [Initiative Tracker](https://github.com/javalent/initiative-tracker) | `initiative-tracker` | TTRPG Initiative Tracker for Obsidian.md |
| [Ink](https://github.com/daledesilva/obsidian_ink) | `ink` | Hand write or draw directly between paragraphs in your notes using a digital pen, stylus, or Apple pencil. Useful for handwriting, sketches, scribbles, or even math equations and scientific notation. Runs on the tldraw framework and drawing provides an infinite canvas. |
| [Ink Player](https://github.com/uglyboy-tl/obsidian-ink-player) | `ink-player` | Playing interactive fiction powered by Inkle's ink engine |
| [Inkporter](https://github.com/AmadeussSystem/Inkporter) | `inkporter` | digitize handwritten notes with intelligent ink isolation, adaptive theming, and automated workflows. |
| [Inline Admonitions](https://github.com/scottTomaszewski/obsidian-inline-admonitions) | `inline-admonitions` | Inline callouts to make text pop. |
| [Inline Callouts](https://github.com/gapmiss/inline-callouts) | `inline-callouts` | Add inline callouts/badges to notes. |
| [Inline Checkbox Groups](https://github.com/bwya77/Inline-Checkbox-Groups) | `inline-checkbox-groups` | Create multiple checkboxes on a single line, separated by a customizable separator character (default '\|'), with the option to automatically cross out text when all checkboxes in the line are checked. |
| [Inline Code Copy](https://github.com/lhinxue/obsidian-inline-code-copy-plugin) | `inline-code-copy` | Copy inline code on click in reading view. |
| [Inline Encrypter](https://github.com/solargate/obsidian-inline-encrypter) | `inline-encrypter` | Encrypt secrets in your notes. |
| [Inline Local Graph](https://github.com/TKOxff/obsidian-inline-local-graph) | `inline-local-graph` | Visualize the local graph inline within your notes. |
| [Inline Scripts](https://github.com/jon-heard/obsidian-inline-scripts) | `obsidian-text-expander-js` | Type text shortcuts which are then replaced with JavaScript generated text. |
| [Inline spoilers](https://github.com/logonoff/obsidian-inline-spoilers) | `inline-spoilers` | Adds Discord-like syntax for inline spoilers. |
| [InlineAI](https://github.com/FBarrca/obsidian-inlineAI) | `inlineai` | AI-powered suggestions, contextual edits, and advanced text transformations directly into your editor. |
| [InlineCodeHighlight](https://github.com/Dimava/inline-code-highlight) | `inline-code-highlight` | Highlight inline `'md **code**` blocks as well as you do the ```md **big**``` ones |
| [Inscribe](https://github.com/ahmetildirim/obsidian-inscribe) | `inscribe` | Inline autocompletion powered by AI. |
| [Insert a New Line Within a Table Cell](https://github.com/marcelflymark/new-line-break-inside-table-cell) | `table-line-break` | Insert a New Line Within a Table Cell |
| [Insert Arknights URL Banner](https://github.com/Rerurate514/insert_ArknightsURL_banners) | `insert-arknights-url-banner` | Select the Arknights image and place it in the banner property. |
| [Insert Heading Link](https://github.com/Signynt/insert-heading-link) | `insert-heading-link` | Add a Link to a Heading |
| [Insert Multiple Attachments](https://github.com/mnaoumov/obsidian-insert-multiple-attachments) | `insert-multiple-attachments` | Allows to insert multiple attachments at a time |
| [Insert New Line](https://github.com/freddyouellette/obsidian-insert-new-line-plugin) | `insert-new-line` | Insert a new line above or below the current line. |
| [InsightA](https://github.com/HongjianTang/obsidian-insighta) | `insighta` | InsightA can transform extensive articles into concise, atomic notes and generate MOC based on note title using LLM. 🚀📝 |
| [Insta TOC](https://github.com/iLiftALot/insta-toc) | `insta-toc` | Simultaneously generate, update, and maintain a table of contents for your notes. |
| [Instant Above Divider](https://github.com/sedationh/obsidian-instant-above-divider) | `instant-above-divider` | Quickly insert a divider line at the beginning of your note. |
| [Instapaper](https://github.com/Instapaper/obsidian-instapaper) | `instapaper` | Connect Obsidian to your Instapaper account. |
| [Intelligence](https://github.com/ransurf/obsidian-intelligence) | `intelligence` | Turn your notes into personalized AI-powered assistants to retrieve ideas, think, and write. Powered by the OpenAI GPT Assistant API. |
| [Interactive Code Blocks](https://github.com/Windesheim-HBO-ICT/Obsidian-Interactive-Code-Block-Plugin) | `interactive-code-blocks` | Preview interactive code blocks! |
| [Interactive Ratings](https://github.com/peritus/obsidian-interactive-ratings) | `interactive-ratings` | Edit symbol ratings in your notes interactively. |
| [Interactivity: Calculations and Scripts](https://github.com/ichichikin/obsidian-plugin-interactivity) | `interactivity` | Interactivity allows you to run shell commands and scripts directly within your notes, providing their output right alongside your written content, making your note-taking process more dynamic and interactive. |
| [Interlinear Glossing](https://github.com/Mijyuoon/obsidian-ling-gloss) | `ling-gloss` | Format interlinear glosses used in linguistics texts. |
| [Invio](https://github.com/frontend-engineering/Invio) | `invio` | Export documents as static websites and deploy to AWS S3 or compatible COS. Streamlining Obsidian Sync and Publish, Invio lets you share notes online, retaining data control via self-hosting. |
| [IOC Lens](https://github.com/acgabbert/IOC-Lens) | `ioc-lens` | Extracts and displays security-relevant indicators such as IP addresses, domains, and file hashes to enhance your cyber security note-taking process. |
| [Iron Vault](https://github.com/iron-vault-plugin/iron-vault) | `iron-vault` | Gameplay plugin/VTT for the Ironsworn/Starforged family of tabletop RPGs. |
| [Itinerary](https://github.com/coddingtonbear/obsidian-itinerary) | `obsidian-itinerary` | Make planning your trip or event easier by rendering a calendar from event information found in your notes. |
| [IVRE](https://github.com/ivre/obsidian-ivre-plugin) | `obsidian-ivre-plugin` | IVRE integration for Obsidian: grab data from IVRE and brings it into Obsidian notes. |
| [Jade Publisher](https://github.com/LucasJi/jade-publisher) | `jade-publisher` | Publish your notes to your Jade service. |
| [Janitor](https://github.com/Canna71/obsidian-janitor) | `janitor` | Performs cleanup tasks on the Obsidian vault |
| [Japanese Manuscript Counter](https://github.com/YoFujii0705/japanese-manuscript-counter) | `japanese-manuscript-counter` | Displays the number of Japanese characters and their equivalent in 400-character manuscript paper in real time. Provides an accurate count taking into account line breaks, paragraphs, and character breaks. |
| [Japanese note taking helper](https://github.com/OverFitted/obsidian-japanese-helper) | `japanese-helper` | Convert romaji to hiragana and katakana to streamline Japanese note‑taking. |
| [Japanese Novel Ruby](https://github.com/k-quels/japanese-novel-ruby) | `japanese-novel-ruby` | Treat ruby(Furigana) ​​marks commonly used in Japanese novels. |
| [JavaScript Init](https://github.com/ryanpcmcquen/obsidian-javascript-init) | `obsidian-javascript-init` | Run JavaScript when Obsidian loads, or any other time. |
| [Jelly Snippets](https://github.com/rabirabirara/obsidian-jelly-snippets) | `jelly-snippets` | A simple plugin for text snippets, with auto replacement |
| [Jira Issue](https://github.com/marc0l92/obsidian-jira-issue) | `obsidian-jira-issue` | This plugin allows you to track the progress of Atlassian Jira issues from your Obsidian notes. |
| [Jira Issue Manager](https://github.com/Alamion/obsidian-jira-sync) | `jira-sync` | Get Jira issues, create and update them. Issue status and worklog management. |
| [Jira Issue managing](https://github.com/angelperezasenjo/obsidian-to-jira) | `jira-issue-managing` | Update and creating of Jira issues directly |
| [Jira Linker](https://github.com/srz2/obsidian-jira-linker) | `jira-linker` | Quickly format a Jira issue tag as a link to you Jira instance. |
| [JIRA links shortener](https://github.com/rplatonovs/obsidian-jira-links-shortener) | `jira-links-shortener` | Modifies pasted JIRA links to use JIRA issue number as the link title |
| [Jisage -Japanese Indentation-](https://github.com/Telehakke/jisage-japanese-indentation) | `jisage-japanese-indentation` | Display 'Jisage' (indenting with a full-width space at the beginning of a line) text correctly. |
| [Journal Folder](https://github.com/chfourie/obsidian-journal-folder) | `journal-folder` | Utilities for folder-based journaling |
| [Journal Review](https://github.com/Kageetai/obsidian-plugin-journal-review) | `journal-review` | Review your daily notes on their anniversaries, like "what happened today last year". |
| [Journaling](https://github.com/Ordeeper/obsidian-journaling-plugin) | `journaling` | View daily notes in a journal-like format, similar to Logseq. It enhances note organization and facilitates better reflection by consolidating daily notes into a continuous journaling view. |
| [Journals](https://github.com/srg-kostyrko/obsidian-journal) | `journals` | Manage your journals in Obsidian |
| [Journalyst](https://github.com/Justin-Arnold/Journalyst) | `journalyst` | Journalyst enables easy creation of topic-specific journals. Organize your life into categories like sleep, routines, or work, with daily or recurring entries for effortless tracking and reflection. |
| [Journey](https://github.com/akaalias/obsidian-journey-plugin) | `obsidian-journey-plugin` | Discover the stories between your notes. |
| [JS Engine](https://github.com/mProjectsCode/obsidian-js-engine-plugin) | `js-engine` | Run JavaScript from within your notes. |
| [JSON table](https://github.com/dario-baumberger/obsidian-json-table) | `json-table` | Simply switch between JSON and tables. Generate a table from a JSON string or a URL (which returns JSON) in your notes. Generate JSON from a table in your notes. |
| [JSON/CSV Importer](https://github.com/farling42/obsidian-import-json) | `obsidian-import-json` | This plugin imports a JSON/CSV file (or text block) and creates notes from a Handlebars template file |
| [JSONifier](https://github.com/KjellConnelly/obsidian-jsonifier) | `obsidian-jsonifier` | Select text that you want to JSON.stringify(), or JSON.parse(). Select text and use the keystroke and the transformation will be copied to your clipboard. Paste it wherever you want. |
| [jTab Guitar Codeblocks](https://github.com/davfive/obsidian-jtab) | `obsidian-jtab` | Adds the ability to show guitar chords and tabs directly in your notes using jTab. |
| [Juggl](https://github.com/HEmile/juggl) | `juggl` | Adds a completely interactive, stylable and expandable graph view to Obsidian. |
| [Julian Date](https://github.com/THeK3nger/obsidian-juliandate) | `obsidian-juliandate` | Simple hotkey to insert the current Julian Date |
| [JuliaPlots](https://github.com/ivnmansi/juliaplots) | `juliaplots` | Plot a function graph inside of your notes using Julia. |
| [Jump to link](https://github.com/mrjackphil/obsidian-jump-to-link) | `mrj-jump-to-link` | This plugin allows open a link in current document or regex based navigation in editor mode using hotkey |
| [Jump-to-Date](https://github.com/TfTHacker/obsidian42-jump-to-date) | `obsidian-jump-to-date-plugin` | Popup calendar for quickly navigating dates |
| [JupyMD](https://github.com/d-eniz/jupymd) | `jupymd` | Use Jupyter notebooks in Obsidian. |
| [Jura Links](https://github.com/justanotherjurastudent/Jura-Links) | `jura-links` | Verlinke deine notierten Gesetzesnormen, Aktenzeichen und Zeitschriften-Fundstellen mit Gesetzesanbietern. |
| [Just Share Please](https://github.com/Ellpeck/ObsidianJustSharePlease) | `just-share-please` | Quickly and easily share individual notes online using an anonymized link. Also easy to self-host! |
| [JW Library Linker](https://github.com/msakowski/obsidian-library-linker) | `jw-library-linker` | Converts JW Library references to actual links in JW Library. |
| [Kale Graph](https://github.com/olillin/obsidian-kale-graph) | `kale-graph` | Render mathematical graphs. |
| [Kanban](https://github.com/obsidian-community/obsidian-kanban) | `obsidian-kanban` | Create markdown-backed Kanban boards in Obsidian. |
| [Kanban Bases View](https://github.com/xiwcx/obsidian-bases-kanban) | `kanban-bases-view` | A kanban-style drag-and-drop custom view for Bases. |
| [Kanban Status Updater](https://github.com/ankit-kapur/obsidian-kanban-status-updater-plugin) | `kanban-status-updater` | Automatically updates a 'status' property in a note when its card is moved on a Kanban board |
| [KaTeX to MathJax](https://github.com/pejakovic/obsidian-convert-katex-to-mathjax) | `convert-katex-to-mathjax` | Converts KaTeX format to MathJax format. |
| [Keep the Rhythm](https://github.com/benjaminezequiel/keep-the-rhythm) | `keep-the-rhythm` | Visualize and track your writing habit! |
| [KeepSidian](https://github.com/lc0rp/KeepSidian) | `keepsidian` | Two-way sync between Obsidian and Google Keep. |
| [Ketcher](https://github.com/yulei-chen/obsidian-ketcher) | `ketcher` | View or draw chemical structures and reactions using Ketcher. |
| [Key Promoter](https://github.com/joethei/obsidian-key-promoter) | `key-promoter` | Learn keyboard shortcuts by showing them when using the mouse |
| [Key Sequence Shortcut](https://github.com/anselmwang/obsidian-key-sequence-shortcut) | `obsidian-key-sequence-shortcut` | Execute obsidian commands with short key sequences. For example, 'tp' for 'Toggle Preview' and 'tb' for 'Toggle Sidebar'. Easier to remember. |
| [Key-Value List](https://github.com/christianwannerstedt/obsidian-key-value-list) | `key-value-list` | Makes it easy to turn lists into formatted key-value lists. |
| [Keyboard Analyzer](https://github.com/cogscides/obsidian-keyboard-analyzer) | `keyboard-analyzer` | See and analyze your keyboard hotkeys and shortcuts |
| [Keyboard Formatter](https://github.com/Lauloque/Keyboard-Formatter) | `keyboard-formatter` | Format selected text into HTML <kbd> tags for representing keyboard keys and mouse inputs. |
| [Keyshots](https://github.com/KrazyManJ/obsidian-keyshots) | `keyshots` | Add classic hotkey/shortcuts commands from popular IDEs like Visual Studio Code or JetBrains Family. |
| [Keyword Highlighter](https://github.com/marcel-goldammer/obsidian-keyword-highlighter) | `keyword-highlighter` | Automatically highlight specified keywords within your Obsidian notes for enhanced visibility and quick reference. |
| [Khoj](https://github.com/khoj-ai/khoj) | `khoj` | Your Second Brain |
| [Kikijiki Habit Tracker](https://github.com/kikijiki/obsidian-habit-tracker) | `kikijiki-habit-tracker` | A simple habit tracker |
| [Kill and Yank](https://github.com/inouetakuya/obsidian-kill-and-yank) | `kill-and-yank` | Enable kill and yank (like Emacs) in the editor |
| [Kindle](https://github.com/SimeonLukas/obsidian-kindle-export) | `obsidian-kindle-export` | Send .md as .mobi to Kindle |
| [Kindle Highlights](https://github.com/hadynz/obsidian-kindle-plugin) | `obsidian-kindle-plugin` | Sync your Kindle book highlights using your Amazon login or uploading your My Clippings file |
| [Kindle Highlights Import](https://github.com/LeonLuttenberger/obsidian-kindle-highlight-import) | `kindle-highlights-import` | Imports the Kindle highlights HTML file and saves it as a note in your vault. |
| [Kindle Highlights Importer](https://github.com/l2xu/kindle_html_importer) | `kindle-html-importer` | Imports the kindle highlights from the html file (you get from the kindle app) into a note in Obsidian. |
| [Kindle Vocab](https://github.com/bao-tg/kindle-vocab) | `kindle-vocab` | Create the Markdown file from your Kindle Vocab Builder in your vault |
| [Kinopoisk search](https://github.com/Alintor/obsidian-kinopoisk-plugin) | `unofficial-kinopoisk` | Helps you find movies and tv shows via Kinopoisk and create notes. |
| [kkh](https://github.com/okikae/obsid-kkh) | `kkh` | Replace words in a string using kkh dictionary. |
| [Kobo Highlights Importer](https://github.com/OGKevin/obsidian-kobo-highlights-import) | `obsidian-kobo-highlights-importer-plugin` | Import highlights from your Kobo device |
| [KOI Sync](https://github.com/metagov/koi-obsidian-plugin) | `koi-sync` | Synchronizes data between networked nodes using the KOI-net protocol. |
| [koncham workspace](https://github.com/manogna4/obsidian-koncham-workspace) | `koncham-workspace` | obsidian workspace enhancements: vertical tabs, and more... |
| [KOReader Highlight Importer](https://github.com/t5k6/obsidian-koreader-highlights) | `koreader-highlights-importer` | Imports KOReader highlights. |
| [KOReader Highlights](https://github.com/Edo78/obsidian-koreader-sync) | `obsidian-koreader-plugin` | This is a plugin for Obsidian. This plugin syncs highlights and notes taken in KOReader. |
| [Korean Book Info](https://github.com/kmsk99/kr-book-info-plugin) | `kr-book-info-plugin` | A plugin that crawls Yes24 to get book information. |
| [Korean Book Search](https://github.com/lazerfit/korean-book-search) | `korean-book-search` | Automatically fills in YAML frontmatter with Korean book information from Aladin API based on the note title. |
| [Korean Spellchecker](https://github.com/dldisud/obsidian-korean-spellchecker) | `korean-spellchecker` | Checks Korean spelling and grammar using an online service. Features a custom dictionary to exclude specific nouns (e.g., names, technical terms) from being flagged as errors. |
| [Kroki](https://github.com/gregzuro/obsidian-kroki) | `obsidian-kroki` | Render Kroki Diagrams |
| [KV Store](https://github.com/Darren-project/obsidian-kv) | `kv-store` | Adds a key-value store. Use it to store and retrieve key-value pairs in your vault. |
| [Lancaster University Week Format](https://github.com/IMB11/ObsidianLUWeeks) | `lancaster-university-week` | (2025-2026 Academic Year) Extends moment.js to provide a custom 'Lancaster University Week' value or 'VACATION' if not in term. Use 'LUW' in the Daily Note format to use! |
| [Language Translator](https://github.com/twentytwokhz/language-translator) | `language-translator` | Translates given text to desired language |
| [LanguageTool](https://github.com/wrenger/obsidian-languagetool) | `languagetool` | Unofficial integration of the LanguageTool spell and grammar checker. |
| [LanguageTool Integration](https://github.com/Clemens-E/obsidian-languagetool-plugin) | `obsidian-languagetool-plugin` | Inofficial LanguageTool plugin |
| [Lapel](https://github.com/liamcain/obsidian-lapel) | `lapel` | Dress up your editor with decorations that mark each of your headings. |
| [Large Language Models](https://github.com/eharris128/Obsidian-LLM-Plugin) | `large-language-models` | Enables access to LLMs via remote providers (OpenAI, Claude, Gemini) and local LLMs via GPT4ALL. |
| [Lark Style CountDown Timer](https://github.com/MoshiQAQ/obsidian-lark-countdown-plugin) | `lark-style-countdown-timer` | Bring Feishu/Lark-style countdown blocks to Obsidian. |
| [Last Edit Location](https://github.com/awfrok/obsidian-plugin-last-edit-location) | `last-edit-location` | Put the cursor at the last edit location when opening a note. Work well with multiple notes. |
| [Last Position](https://github.com/Saktawdi/obsidian-last-position) | `last-position` | Automatically scroll to the last viewed position when opening the Markdown document. |
| [LaTeX Algorithms](https://github.com/SamZhang02/obsidian-latex-algorithms) | `latex-algorithms` | Plugin to facilitate writing algorithm blocks in LaTeX |
| [LaTeX autocomplete](https://github.com/Yanis-Gerst/latex-autocomplete) | `latex-autocomplete` | Simple auto-completion for LaTeX. As simple as typing '\'. |
| [Latex Environments](https://github.com/raineszm/obsidian-latex-environments) | `obsidian-latex-environments` | Allows to quickly insert and change latex environments within math environments. |
| [Latex Exporter](https://github.com/mscott99/Latex-Exporter) | `latex-exporter` | Write a LaTeX paper. |
| [LaTeX Math](https://github.com/zarstensen/obsidian-latex-math) | `latex-math` | Evaluate, solve and much more within LaTeX blocks using Sympy. |
| [Latex Matrices](https://github.com/Deltekk/Obsidian-Latex-Matrices) | `latex-matrices` | Speedup latex matrices writing. |
| [Latex OCR](https://github.com/lucasvanmol/obsidian-latex-ocr) | `latex-ocr` | Generate LaTeX equations from images in your vault or clipboard. |
| [LaTeX Panel Helper](https://github.com/myluster/Obsidian-LaTeX-Helper) | `latex-panel-helper` | Provides a convenient panel with categorized LaTeX symbols, real-time search, and a pop-out window to enhance your mathematical note-taking efficiency! |
| [Latex Render](https://github.com/jvsteiner/obsidian-latex-render) | `latex-render` | Render snippets of latex code as SVG files. |
| [Latex Suite](https://github.com/artisticat1/obsidian-latex-suite) | `obsidian-latex-suite` | Make typesetting LaTeX math as fast as handwriting through snippets, text expansion, and editor enhancements |
| [LaTeX to Unicode converter](https://github.com/fjdu/obsidian-latex-unicode) | `latex-to-unicode` | Convert LaTeX commands into unicode sqeuences |
| [LaTeX-like Theorem & Equation Referencer](https://github.com/RyotaUshio/obsidian-latex-theorem-equation-referencer) | `math-booster` | A powerful indexing & referencing system for theorems & equations in your vault. Bring LaTeX-like workflow into Obsidian with theorem environments, automatic equation numbering, and more. |
| [LaTeX-OCR](https://github.com/JackBarker7/obsidian-latexocr) | `latexocr` | Run LaTeX-OCR if it is installed locally. |
| [Lava VTT Uploader](https://github.com/lavaforge/obsidian-lava-vtt-uploader) | `lava-vtt-uploader` | Display images from your vault in Lava VTT. |
| [Lavadocs](https://github.com/SaalikLok/lavadocs-obsidian) | `lavadocs` | Public docs, from the fires of your vault. |
| [LawList: Custom List Styles](https://github.com/willem-schlieter/lawlist) | `lawlist` | Adds support for freely configurable, custom list styles (Edit Mode and Read Mode). |
| [Laws of Form](https://github.com/Kevger/obsidian-laws-of-form) | `laws-of-form` | Allows you to create, manage and display Laws of Form expressions like ((a)) (b) = a (b). |
| [Layout Manager](https://github.com/ShadiestGoat/obsidian-layout-manager) | `layout-manager` | Manage layouts with context |
| [Lazy Plugin Loader](https://github.com/alangrainger/obsidian-lazy-plugins) | `lazy-plugins` | Load plugins with a delay on startup, so that you can get your app startup down into the sub-second loading time. |
| [LDS Library Reference](https://github.com/ingiestein/obsidian-lds-scriptures-plugin) | `lds-library-reference` | Easily insert references to scripture and conference talks from the Church of Jesus Christ of Latterday Saints |
| [LDS Library Reference](https://github.com/pacokwon/obsidian-lds-library-plugin) | `lds-scriptures-reference` | Easily insert references to scripture and conference talks from the Church of Jesus Christ of Latter-day Saints |
| [Leader Hotkeys](https://github.com/tgrosinger/leader-hotkeys-obsidian) | `leader-hotkeys-obsidian` | Add leader hotkey support to any command (like tmux or vim) |
| [Leaflet](https://github.com/javalent/obsidian-leaflet) | `obsidian-leaflet-plugin` | Interactive maps inside your notes |
| [Lean Syntax Highlight](https://github.com/tomaz1502/lean-syntax-highlight) | `lean-syntax-highlight` | Provides live syntax highlight for the Lean programming language |
| [Learnie](https://github.com/tankh99/learnie-plugin) | `learnie` | Enhance your learning with active recall and spaced repetition. Track changes, create review questions, and streamline your study process for more effective, long-lasting learning. |
| [Ledger](https://github.com/tgrosinger/ledger-obsidian) | `ledger-obsidian` | Plain text accounting |
| [Lemons Search](https://github.com/mProjectsCode/obsidian-lemons-search-plugin) | `lemons-search` | A blazingly fast fuzzy finder with file preview. |
| [Letterboxd Diary RSS Sync](https://github.com/Fleker/letterboxd-for-obsidian) | `letterboxd-rss-sync` | Syncs your public Letterboxd diary. |
| [Life in Weeks Calendar](https://github.com/szuc/obsidian-life-in-weeks-calendar) | `life-in-weeks-calendar` | Display your entire life in weeks, with weekly notes integration. |
| [LifeOS](https://github.com/quanru/obsidian-lifeos) | `periodic-para` | Life management system(Assist in practicing the PARA method with periodic notes and usememos). |
| [LighterPack importer](https://github.com/nsiniscalchi/LighterPackObsidianImporter) | `lighterpack-importer` | Import a packing list from https://lighterpack.com. |
| [Lilypond](https://github.com/dot-asterisk-nl/obsidian-lilypond) | `lilypond` | Lilypond support in Obsidian |
| [Limelight](https://github.com/smikula/obsidian-limelight) | `obsidian-limelight` | Put a spotlight on your active pane |
| [Limitless Lifelogs](https://github.com/Maclean-D/obsidian-limitless-lifelogs) | `limitless-lifelogs` | Sync your Limitless AI lifelog entries |
| [Line Arrange](https://github.com/chitwan27/lineArrange) | `line-arrange` | Shuffle, reverse, or sort text, using either visual width or alphabetical order. |
| [Line Commands](https://github.com/charliecm/obsidian-line-commands) | `line-commands` | Adds commands to quickly select, copy, cut, and paste lines under the selection or cursor. |
| [LINE Notes Sync](https://github.com/onikun94/line_to_obsidian) | `line-notes-sync` | Sync messages from LINE to your notes. |
| [Lineage](https://github.com/ycnmhd/obsidian-lineage) | `lineage` | Edit Markdown in a keyboard-centric Miller columns interface. Inspired by Gingko Writer. |
| [Linear](https://github.com/caseybecking/obsidian-linear-plugin) | `linear` | Integrate Linear issues with advanced filtering, sorting, and visual enhancements. Features include due date indicators, status colors, and comprehensive debug logging. |
| [Linear Integration](https://github.com/casals/obsidian-linear-integration-plugin) | `linear-integration` | Sync Linear (https://linear.app) issues with notes. Create, update, and track Linear issues directly from your vault. |
| [Lineup Builder](https://github.com/James-Fallon/obsidian-lineup-builder) | `obsidian-lineup-builder` | Build football lineups in Obsidian. |
| [Link Archive](https://github.com/tomzorz/obsidian-link-archive) | `obsidian-link-archive` | This plugin archives links in your note so they're available to you even if the original site goes down or gets removed. |
| [Link Converter](https://github.com/ozntel/obsidian-link-converter) | `obsidian-link-converter` | Scan all your links in the vault and convert them to your desired format. |
| [Link Embed](https://github.com/Seraphli/obsidian-link-embed) | `obsidian-link-embed` | This plugin auto-fetches page metadata to embed Notion-style link preview cards. |
| [Link Exploder](https://github.com/benhughes/obsidian-link-exploder) | `link-exploder` | Link Exploder is a Obsidian plugin that creates a canvas from a note, embedding it's incoming (i.e. backlinks) and outgoing links onto the canvas (as well as the their linked notes). |
| [Link Favicons](https://github.com/joethei/obsidian-link-favicon) | `link-favicon` | See the favicon for a linked website. |
| [Link Formatter](https://github.com/dilantha/link-formatter) | `link-formatter` | Formats a block of links into a clean markdown list |
| [Link indexer](https://github.com/aviskase/obsidian-link-indexer) | `obsidian-link-indexer` | Generate index notes with links based on various conditions |
| [Link Maintainer](https://github.com/wenlzhang/obsidian-link-maintainer) | `link-maintainer` | Maintain note links when splitting or reorganizing notes. |
| [Link Navigation](https://github.com/xRyul/link-navigation) | `link-navigation` | Navigate between incoming links (inlinks), outgoing links (outlinks) N levels deep. Links from Canvas are also supported. |
| [Link Opening Restore](https://github.com/SmallZombie/link-opening-restore) | `link-opening-restore` | Make links require Ctrl + Left Click to open. |
| [Link Preview](https://github.com/felipetappata/obsidian-link-preview) | `link-preview` | Show a preview of external links on hover |
| [Link Range](https://github.com/rmellmer/obsidian-link-range) | `link-range` | This Obsidian plugin brings ranged link support to Obsidian. |
| [Link Remover](https://github.com/AlphaHasher/obsidian-remove-links) | `hyperlink-remover` | Easily remove hyperlinks and wikilinks from selected text or the entire note. |
| [Link to Verse](https://github.com/aygjiay/obsidian-link-to-verse) | `link-to-verse` | From a Bible reference selected, creates a markdown link to a configured Bible site. |
| [Link Tree](https://github.com/j-palindrome/obsidian-link-tree) | `link-tree` | View file links and backlinks as a recursively expandable, filterable list with editable text, combining the structure of outliners like Dynalist & WorkFlowy with the flexibility of Obsidian. |
| [Link with alias](https://github.com/pvojtechovsky/obsidian-link-with-alias) | `link-with-alias` | Creates links and aliases in front matter of target document |
| [Linked Data Helper](https://github.com/kometenstaub/linked-data-helper) | `linked-data-helper` | Parse Linked data for Linked Data Vocabularies. |
| [Linked Data Vocabularies](https://github.com/kometenstaub/linked-data-vocabularies) | `linked-data-vocabularies` | Add linked data (LCSH) as metadata to your notes. |
| [Linked Note Exporter](https://github.com/the-c0d3r/obsidian-linked-note-exporter) | `linked-note-exporter` | Export note with all its attachments and linked notes. |
| [Linkify](https://github.com/matthewhchan/linkify) | `linkify` | Converts matching text into links. |
| [LinkMagic](https://github.com/AndyReifman/LinkMagic) | `link-magic` | Automatically adds links to defined regex. |
| [Links](https://github.com/mii-key/obsidian-links) | `links` | Manipulate links |
| [LinkStowr](https://github.com/joelseq/obsidian-linkstowr) | `linkshelf` | Save links from your browser directly into Obsidian. |
| [Linter](https://github.com/platers/obsidian-linter) | `obsidian-linter` | Formats and styles your notes. It can be used to format YAML tags, aliases, arrays, and metadata; footnotes; headings; spacing; math blocks; regular markdown contents like list, italics, and bold styles; and more with the use of custom rule options as well. |
| [Liquid Templates](https://github.com/oeN/liquid-template) | `liquid-templates` | Empower your template with LiquidJS tags |
| [List Callouts](https://github.com/mgmeyers/obsidian-list-callouts) | `obsidian-list-callouts` | Create simple callouts in lists. |
| [List Modified](https://github.com/franciskafieh/obsidian-list-modified) | `obsidian-list-modified` | The advanced and adaptive changelog. Links all modified files meeting certain criteria to a timed (daily, weekly, monthly) note. |
| [List Outline Helper](https://github.com/triangular-sneaky/obsidian-list-outline-helper) | `list-outline-helper` | Utilities to work with list outlines. Currently supports selecting the outline (current line and children) |
| [List to table converter](https://github.com/paddomanno/obsidian-list-table-converter) | `list-table-converter` | Convert a list (or multi-line text) to a table. |
| [Listen Up!](https://github.com/tejas-hosamani/obsidian-plugin-text-to-speech) | `listen-up` | Covert text to natural voice audio, locally - Listen Up! |
| [Lite Gallery](https://github.com/jpoles1/obsidian-litegal) | `litegallery` | Easily create carousel galleries to better organize/view images in your notes. |
| [LiteCite](https://github.com/ras0q/obsidian-litecite) | `litecite` | Creates citation notes from a BibTeX / BibLaTeX file |
| [Literate Haskell](https://github.com/jajaperson/obsidian-literate-haskell) | `literate-haskell` | An obsidian plugin for integrating `.lhs` files into your PKM. |
| [Live Background](https://github.com/remememe/Live-Wallpaper) | `live-wallpaper` | Add dynamic live wallpapers (images/videos) to your workspace with customizable effects |
| [Live Variables](https://github.com/HamzaBenyazid/Live-variables) | `live-variables` | Define variables in your note's properties and reuse them throughout your content. |
| [Livecodes Playground](https://github.com/gapmiss/livecodes-playground) | `livecodes-playground` | Client-side code editor playground - Powered by LiveCodes |
| [Living Graph](https://github.com/geoffreysflaminglasersword/obsidian-living-graph) | `obsidian-living-graph` | A for-fun graph plugin |
| [LLM docs](https://github.com/shane-lamb/obsidian-llm-docs) | `llm-docs` | Simple LLM (AI) client using pure markdown documents |
| [LLM Shortcut](https://github.com/chernodub/obsidian-llm-shortcut) | `llm-shortcut` | Provides a way to create shortcuts for commands powered by LLM capabilities. |
| [LLM Summary](https://github.com/larksq/obsidian-llm-summary) | `llm-summary` | Quick note taking with the help of LLMs. LLMs help you to summarize / organize PDFs or existing notes. |
| [LLM Tagger](https://github.com/djayatillake/obsidian-llm-tagger) | `llm-tagger` | Automatically tag your notes using local LLMs via Ollama |
| [LLM Test Generator](https://github.com/aldo-g/obsidian-llm-test) | `llm-test-gen` | Generate AI-powered test questions from your notes with latest LLM models (OpenAI, Claude, Mistral, Gemini, DeepSeek, Ollama). Automatically fetches newly released models. Any language support. |
| [LLM workspace](https://github.com/ofalvai/obsidian-llm-workspace) | `llm-workspace` | Use Large Language Models grounded in your notes. |
| [Local Any Files](https://github.com/ShermanTsang/obsidian-local-any-files) | `local-any-files` | Download all files from links to local attachments. |
| [Local Backup](https://github.com/velviagris/obsidian-local-backup) | `local-backup` | Automatically creates a local backup of the vault. |
| [Local Bible Ref](https://github.com/camelChief/local-bible-ref) | `local-bible-ref` | Quickly and easily reference Bible passages stored locally in your vault. |
| [Local File Interface](https://github.com/qawatake/obsidian-local-file-interface-plugin) | `obsidian-local-file-interface-plugin` | Provides commands for moving files in and out of the vault |
| [Local GPT](https://github.com/pfrankov/obsidian-local-gpt) | `local-gpt` | Local GPT assistance for maximum privacy and offline access |
| [Local images](https://github.com/aleksey-rezvov/obsidian-local-images) | `obsidian-local-images` | Searches your notes for hotlinked images, downloads, saves them locally than fix tags in md-files. |
| [Local Images Plus](https://github.com/Sergei-Korneev/obsidian-local-images-plus) | `obsidian-local-images-plus` | Local Images Plus plugin searches for all external media links in your notes, downloads and saves them locally and adjusts the links in your notes to point to the saved files. |
| [Local LLM Helper](https://github.com/manimohans/obsidian-local-llm-helper) | `local-llm-helper` | Use your own secure local LLM server to work with your text! |
| [Local Media Embedder](https://github.com/seyf1elislam/obsidian-LocalMediaEmbedder-plugin) | `local-media-embedder` | Embed videos and images and audios from your local device  in your notes. |
| [Local Quotes](https://github.com/sundevista/local-quotes) | `local-quotes` | Collect your quotes from all over the repository and embed them in different locations with refresh delays. |
| [Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api) | `obsidian-local-rest-api` | Get, change or otherwise interact with your notes in Obsidian via a REST API. |
| [Local RSS](https://github.com/onikun94/obsidian-local-rss) | `local-rss` | Download RSS feed articles to local files. |
| [Lock Screen](https://github.com/ericbiewener/obsidian-lock-screen-plugin) | `obsidian-lock-screen-plugin` | Protect your vault with a lock screen. |
| [Log Keeper](https://github.com/JimJamBimBam/obsidian-log-keeper) | `log-keeper` | Generate time stamps automatically as changes are made to a note. |
| [logos-refs](https://github.com/joey-kilgore/logos-refs) | `logos-refs` | Easily take refs from Logos and connect them within your notes |
| [Logstravaganza](https://github.com/czottmann/obsidian-logstravaganza) | `logstravaganza` | A simple proxy for `console.*()` calls which copies log messages and uncaught exceptions to a file. |
| [Long sentence highlighter](https://github.com/RobertMeissner/obsidian-long-sentence-highlighter) | `long-sentence-highlighter` | Highlights sentences that exceed a configurable word count threshold to help improve writing clarity and readability. |
| [Longform](https://github.com/kevboh/longform) | `longform` | Write novels, screenplays, and other long projects in Obsidian. |
| [LongtimeDiary](https://github.com/sawamaru/obsidian-LongtimeDiary) | `longtime-diary` | Show past Daily notes on the same day in previous years. |
| [Lookalike](https://github.com/jlweston/obsidian-note-proximity-plugin) | `note-promixity` | Find similar notes based on the frequency of terms within the vault. |
| [Loom](https://github.com/cosmicoptima/loom) | `loom` | Loom in Obsidian |
| [Lovely-Mindmap](https://github.com/shaunhurryup/lovely-mindmap) | `lovely-mindmap` | Build your own knowledge graph with smiles :-) |
| [Lskypro Upload V2](https://github.com/Aceak/Lskypro-Upload-V2) | `lskypro-upload-v2` | Auto upload local images to LskyPro. |
| [Luhman](https://github.com/Dyldog/luhman-obsidian-plugin) | `luhman` | Commands for handling a zettelkasten with Luhmann-style IDs as filenames |
| [Lumberjack 🪓 🪵](https://github.com/ryanjamurphy/lumberjack-obsidian) | `lumberjack-obsidian` | Log your thoughts! Lumberjack adds URL commands to help you axe inefficiency and get right to writing. |
| [Lunar Calendar](https://github.com/WHG555/lunar-calendar) | `lunar-calendar` | 一个支持农历的日历 |
| [Lyrics](https://github.com/eatgrass/obsidian-lyrics) | `lyrics` | Enhance the audio player with interacive lyrics |
| [Légifrance Intégration](https://github.com/carnetdethese/legifrance-integration) | `legifrance-integration` | Intégration de l'API Légifrance. |
| [macOS Keyboard Navigation](https://github.com/ryanjamurphy/macOS-keyboard-nav-obsidian) | `macOS-keyboard-nav-obsidian` | This plugin adds alt+up arrow and alt+down arrow keyboard navigation to Obsidian. |
| [Macros](https://github.com/JamesCliffordSpratt/macros) | `macros` | Track daily nutrition, calories, protein, fat, and carbs with interactive tables and charts. Create meal templates, search foods via FatSecret API, and visualize macro data with customizable pie charts and multi-day analytics. |
| [Magic Move](https://github.com/imfenghuang/obsidian-magic-move) | `magic-move` | Animating code blocks with markdown and code syntax highlighting with beautiful themes. |
| [MagicCalendar](https://github.com/Vaccarini-Lorenzo/MagicCalendar) | `magic-calendar` | AI-Powered Obsidian Plugin that leverage Natural Language Processing techniques to find calendar events in Markdown notes, seamlessly synchronizing them with a calendar of choice. |
| [Magiedit](https://github.com/magitools/magiedit-obsidian) | `magiedit` | Official integration for Magiedit's API |
| [Mahgen Renderer](https://github.com/MichaelFW-ui/mahgen-renderer) | `mahgen-renderer` | Display mahjong images inline or in block using Mahgen. |
| [Mahjong Renderer](https://github.com/h-sphere/obsidian-mahjong-renderer) | `mahjong-renderer` | Render mahjong tiles (riichi mahjong) using MPSZ algebraic notation |
| [make.md](https://github.com/Make-md/makemd) | `make-md` | make.md gives you everything you need to organize and personalize your notes. |
| [ManicTime](https://github.com/manictime/manictime-obsidian) | `manictime` | Sends path of active file to locally installed ManicTime client. |
| [MantouAI](https://github.com/ravenSanstete/Obsidian-MantouAI) | `mantou-ai` | Work as a personal assistant for translation, writing polish, general Q&A, summarizing, using the power of large language models. |
| [Manual Sorting](https://github.com/kh4f/manual-sorting) | `manual-sorting` | Drag'n'Drop sorting within file explorer. |
| [Map of Content](https://github.com/Robin-Haupt-1/Obsidian-Map-of-Content) | `map-of-content` | Automatically generate a Map of Content for your vault |
| [Map View](https://github.com/esm7/obsidian-map-view) | `obsidian-map-view` | An interactive map view. |
| [Mapbox Location Image](https://github.com/aaronczichon/obsidian-location-plugin) | `mapbox-location` | Show a map inside your notes with a specific format. |
| [Maps](https://github.com/obsidianmd/obsidian-maps) | `maps` | Adds a map layout to bases so you can display notes as an interactive map view. |
| [Mark and Select](https://github.com/anselmwang/obsidian-mark-and-select) | `obsidian-mark-and-select` | More flexible ways to select texts in Obsidian Editor |
| [Mark Open Files](https://github.com/gasparschott/obsidian-mark-open-files) | `mark-open-files` | Enhances the File Explorer by adding a marker to all the File Explorer items that are currently open in the workspace. |
| [Markdoc](https://github.com/kamoshi/obsidian-markdoc) | `markdoc` | Basic support for Markdoc files |
| [Markdown Attributes](https://github.com/javalent/markdown-attributes) | `markdown-attributes` | Add markdown attributes to elements in Obsidian.md |
| [Markdown Blogger](https://github.com/afazio1/obsidian-markdown-blogger) | `markdown-blogger` | Allows developers to push markdown notes to their local blog, portfolio, or static site. Works with Astro.js, Next.js, and any other framework configured to render markdown pages. |
| [Markdown Calendar Generator](https://github.com/zachatrocity/md-cal-gen) | `md-cal-gen` | An intentionally simple markdown table calendar generator |
| [Markdown Chords](https://github.com/dnotes/obsidian-markdown-chords) | `markdown-chords` | Add musical chord notation and chord diagrams for stringed instruments (e.g. guitar) in Markdown. Supports chords in any Western scale/mode, including extended jazz chords. |
| [markdown export](https://github.com/bingryan/obsidian-markdown-export-plugin) | `obsidian-markdown-export-plugin` | This is a markdown export plugin for Obsidian. |
| [Markdown Formatting Assistant](https://github.com/Reocin/obsidian-markdown-formatting-assistant-plugin) | `obsidian-markdown-formatting-assistant-plugin` | This Plugin provides a simple Editor for Markdown, HTML and Colors and in addition a command interface. The command interface facilitate a faster workflow. |
| [Markdown Furigana](https://github.com/steven-kraft/obsidian-markdown-furigana) | `obsidian-markdown-furigana` | Simple Markdown to Furigana Rendering Plugin for Obsidian. |
| [Markdown Image Caption](https://github.com/HananoshikaYomaru/obsidian-image-caption) | `md-image-caption` | Generate image caption |
| [Markdown Link Space Encoder](https://github.com/rkosova/obsidian-markdown-link-space-encoder) | `markdown-link-space-encoder` | Simple plugin to automatically encode spaces to %20 in Markdown-style links |
| [Markdown Media Card](https://github.com/zhouhua/obsidian-markdown-media-card) | `markdown-media-card` | Insert media information cards in Markdown, such as books, music, movies, etc. |
| [Markdown prettifier](https://github.com/cristianvasquez/obsidian-prettify) | `markdown-prettifier` | Tries to fix and reformat ugly Markdown and adds things like 'modified date' etc. |
| [Markdown shortcuts](https://github.com/JulesGuesnon/obsidian-markdown-shortcuts) | `markdown-shortcuts` | Allows to write markdown from shortcuts (example: >h1 -> #). |
| [Markdown Sync Scroll](https://github.com/XeroAlpha/markdown-sync-scroll) | `markdown-sync-scroll` | Allow two linked markdown views to scroll synchronously. |
| [Markdown table checkboxes](https://github.com/0x-DLN/obsidian-table-checkboxes) | `table-checkboxes` | Converts markdown checkboxes in tables to HTML, and reflects the state upon (un)checking them. |
| [Markdown Table Editor](https://github.com/ganesshkumar/obsidian-table-editor) | `markdown-table-editor` | An Obsidian plugin to provide an editor for Markdown tables. It can open CSV, Microsoft Excel/Google Sheets data as Markdown tables from Obsidian Markdown editor. |
| [Markdown Timeline](https://github.com/recklyss/markdown-timeline) | `markdown-timeline` | Convert markdown into timeline visualization |
| [Markdown to Jira Converter](https://github.com/muckmuck96/obsidian-md-to-jira) | `obsidian-md-to-jira` | This is a markdown to jira markup and backwards converter plugin for Obsidian (https://obsidian.md) |
| [Markdown to Slack Message](https://github.com/idreamer/markdown-to-slack-message) | `markdown-to-slack-message` | This plugin converts a markdown note to the Slack message blocks that enables you to send to your slack |
| [Markdown Tree](https://github.com/carvah/markdown-tree-plugin) | `markdown-tree` | Create a beautiful and intuitive directory tree using Markdown-oriented code style using tabs, spaces and enters. |
| [Markitdown File Converter](https://github.com/ethanolivertroy/obsidian-markitdown) | `markitdown` | Convert PDFs, Office documents, images, and other file formats to Markdown using Microsoft's Markitdown tool |
| [Markline](https://github.com/hotoo/obsidian-markline) | `markline` | Timeline view from markdown. |
| [Markmap to CSV](https://github.com/pj4316/markmap-to-csv-obsidian) | `markmap-to-csv` | Converts Markmap data to CSV format. |
| [Markmind](https://github.com/MarkMindCkm/obsidian-markmind) | `obsidian-markmind` | This is a mindmap , outline tool for obsidian. |
| [Markpilot](https://github.com/taichimaeda/markpilot) | `markpilot` | Inline completions and chat view powered by OpenAI |
| [Markwhen](https://github.com/mark-when/obsidian-plugin) | `markwhen` | Create timelines, gantt charts, calendars, and more using markwhen. |
| [Markwhen File Sync](https://github.com/rouvenjahnke/markwhen-file-sync) | `markfilesync` | Synchronize properties from your notes with a Markwhen timeline file |
| [Marp](https://github.com/JichouP/obsidian-marp-plugin) | `marp` | Plugin for using Marp on Obsidian. |
| [Marp Slides](https://github.com/samuele-cozzi/obsidian-marp-slides) | `marp-slides` | Create markdown-based Marp presentations in Obsidian |
| [Masking Type](https://github.com/Telehakke/masking-type) | `masking-type` | Mask bold, italic, and highlight |
| [Mass Create](https://github.com/vellikhor/mass-create) | `mass-create` | Create large quantities of notes easily at one time. |
| [Mastodon Threading](https://github.com/elpamplina/mastodon-threading) | `mastodon-threading` | Compose and post threads to Mastodon. |
| [MatchSyntax](https://github.com/rivea0/obsidian-match-syntax) | `match-syntax` | A flexible, regex-like lookups for your notes. |
| [Material Symbols](https://github.com/cberane/obsidian-material-symbols) | `material-symbols` | This plugin adds the material symbols (outlined) to obsidian |
| [Math Indicator Changer](https://github.com/Ori-Replication/obsidian-math-indicator-changer) | `math-indicator-changer` | Change the math indecator from parentheses&brackets to $, make the math formula generated by GPT & Other AI display correctly. |
| [Math+](https://github.com/ocapraro/obsidian-math-plus) | `obsidian-math-plus` | This is an Obsidian plugin for taking math notes using Excalidraw. |
| [Mathematica Plot](https://github.com/MarcosNicolau/obsidian-mathematica-plot) | `mathematica-plot` | Render graphs using Wolfram Mathematica code! |
| [MathLive](https://github.com/danzilberdan/obsidian-mathlive) | `mathlive` | Faster and more intuitive MathJax editing using MathLive. |
| [MathLive in Editor Mode](https://github.com/MizarZh/mathlive-in-editor-mode) | `mathlive-in-editor-mode` | MathLive input in editor mode |
| [Mathpad](https://github.com/Canna71/obsidian-mathpad) | `mathpad` | Computer Algebra System and Calculator for Obsidian |
| [MathType](https://github.com/slateblua/mathtype) | `mathtype` | Allows to type math faster with on the fly suggestions |
| [Matter](https://github.com/getmatterapp/obsidian-matter) | `matter` | The official Matter <> Obsidian plugin |
| [Maximise Active Pane](https://github.com/deathau/maximise-active-pane-obsidian) | `maximise-active-pane-obsidian` | Simply fills the workspace with the active pane |
| [MBlog Publish](https://github.com/kingwrcy/obsidian-mblog) | `mblog-publish` | 发布文章到MBlog平台,目前支持单篇文章发布 |
| [MCP Tools](https://github.com/jacksteamdev/obsidian-mcp-tools) | `mcp-tools` | Securely connect Claude Desktop to your vault with semantic search, templates, and file management capabilities. |
| [MDX](https://github.com/yulei-chen/obsidian-mdx) | `mdx` | Preview MDX in Obsidian, with support for Code Hike |
| [mdx as md](https://github.com/mkozhukharenko/mdx-as-md-obsidian) | `mdx-as-md-obsidian` | Edit mdx files as if they were markdown |
| [Meal Plan](https://github.com/tmayoff/obsidian-meals) | `tmayoff-meals` | Store and manage recipes, create weekly meal plans and generate shopping lists. |
| [Media Companion](https://github.com/Nick-de-Bruin/obsidian-media-companion) | `media-companion` | Creates a searchable gallery and sidecar files for attachments such as images and videos. The sidecar files allow you to add notes and tags to your media files. |
| [Media DB](https://github.com/mProjectsCode/obsidian-media-db-plugin) | `obsidian-media-db-plugin` | A plugin that can query multiple APIs for movies, series, anime, games, music and wiki articles, and import them into your vault. |
| [Media Extended](https://github.com/aidenlx/media-extended) | `media-extended` | Media(Video/Audio) Playback Enhancement for Obsidian.md |
| [Media Notes](https://github.com/jemstelos/obsidian-media-notes) | `media-notes` | Take notes on YouTube videos and podcasts with media controls and timestamps. |
| [Media Slider](https://github.com/amatya-aditya/obsidian-media-slider) | `media-slider` | A media slider for images, gifs, audios, videos, and PDFs. |
| [Media Sync](https://github.com/fnya/media-sync) | `media-sync` | Downloads media files(eg. images, PDFs) from the URLs in documents and displays the content. |
| [Media Viewer](https://github.com/Devon22/obsidian-mediaviewer) | `mediaviewer` | View and manage media files within your notes. |
| [Medium Importer](https://github.com/arumie/obsidian-medium-importer-plugin) | `medium-importer` | Import Medium posts into your vault |
| [Mehrmaid](https://github.com/huterguier/obsidian-mehrmaid) | `mehrmaid` | Enables you to put Markdown inside of Mermaid diagrams. |
| [Meld Build](https://github.com/meld-cp/obsidian-build) | `meld-build` | Write and execute (sandboxed) JavaScript to render templates, query DataView and create dynamic notes. |
| [Meld Calc](https://github.com/meld-cp/obsidian-calc) | `meld-calc` | Do math |
| [Meld Encrypt](https://github.com/meld-cp/obsidian-encrypt) | `meld-encrypt` | Hide secrets in your vault |
| [MemoChron](https://github.com/formax68/memoChron) | `memochron` | Calendar integration and note creation with support for public iCalendar URLs |
| [Memodack](https://github.com/memodack/memodack) | `memodack` | Your second language memory tool |
| [Memories](https://github.com/DIMFLIX/obsidian-memories) | `memories` | Display media galleries with images, videos, and audio directly in notes. |
| [Memorization](https://github.com/nwindian/Memorization-Plugin) | `memorization` | Generates study index notes using a spaced repetition algorithm (SM-2). |
| [MemoryLane](https://github.com/bangca85/obsidian-memorylane-plugin) | `vn-memory-lane` | Relive and celebrate your life's milestones on a personal, interactive timeline. A nostalgic journey through your history with anniversary reminders and cherished memories. |
| [Memos AI Sync](https://github.com/leoleelxh/obsidian-memos-ai-sync) | `memos-ai-sync` | Sync Memos content with AI enhancement |
| [Memos Sync](https://github.com/RyoJerryYu/obsidian-memos-sync) | `memos-sync` | Syncing memos from a [Memos](https://github.com/usememos/memos) server to your daily note. Fully compatible with official Daily Notes plugin, Calendar plugin and Periodic Notes plugin. |
| [Mention Things](https://github.com/stracker-phil/obsidian-mention-things) | `mention-things` | Define a list of prefixes to trigger an autocomplete suggestion to insert a link. |
| [Merge Notes](https://github.com/fnya/merge-notes) | `merge-notes` | Merge the selected notes. |
| [Mermaid Icons](https://github.com/toshs/obsidian-mermaid-icons) | `mermaid-icons` | Use Font Awesome and other icon sets within your Mermaid diagrams. |
| [Mermaid Themes](https://github.com/jvsteiner/mermaid-themes) | `mermaid-themes` | Makes it easy to apply custom mermaid.js themes and apply other tweaks. This plugin is supported by advertisements. |
| [Mermaid Tools](https://github.com/dartungar/obsidian-mermaid) | `mermaid-tools` | Improved Mermaid.js experience for Obsidian: visual toolbar with common elements & more |
| [Mermaid.js Helper (OMH)](https://github.com/FrancescoDiCursi/Mermaid.js-Helper-OMH-plugin) | `mermaid-helper` | plug in that helps in mermaid.js workflow and more |
| [Mesh AI](https://github.com/chasebank87/mesh-ai) | `mesh-ai` | Mesh AI prompt manager and gererator |
| [Messager](https://github.com/xiaotianhu/obsidian-messager) | `messager` | Save messages into vault which sending through WeChat / HTTP API / Email |
| [Meta Bind](https://github.com/mProjectsCode/obsidian-meta-bind-plugin) | `obsidian-meta-bind-plugin` | Make your notes interactive with inline input fields, metadata displays, and buttons. |
| [Metadata Auto Classifier](https://github.com/GoBeromsu/Metadata-Auto-Classifier) | `metadata-auto-classifier` | Automatically classifies and applies metadata to your notes. |
| [Metadata Extractor](https://github.com/kometenstaub/metadata-extractor) | `metadata-extractor` | Metadata export on a schedule for integration with third-party apps like launchers. |
| [Metadata Hider](https://github.com/Benature/obsidian-metadata-hider) | `metadata-hider` | Hide specific metadata property or if its value is empty. |
| [Metadata Icon](https://github.com/Benature/obsidian-metadata-icon) | `metadata-icon` | Change metadata entry icon |
| [Metadata Menu](https://github.com/mdelobelle/metadatamenu) | `metadata-menu` | For data quality enthusiasts (and dataview users): manage the metadata of your notes. |
| [MetaEdit](https://github.com/chhoumann/MetaEdit) | `metaedit` | MetaEdit helps you manage your metadata. |
| [Metafolders](https://github.com/makary-s/obsidian-metafolders) | `metafolders` | Multidimensional note navigation |
| [Metal Archives (Unofficial)](https://github.com/vincenzocaputo/obsidian-metal-archives-plugin) | `metal-archives` | Create notes about metal bands and album from Metal Archives |
| [Metronome](https://github.com/curtgrimes/obsidian-metronome-plugin) | `obsidian-metronome-plugin` | Add interactive metronomes to your notes. |
| [Micro templates](https://github.com/epszaw/obsidian-micro-templates) | `micro-templates` | Flexible embedded micro templates powered by javascript functions |
| [Micro.publish](https://github.com/otaviocc/obsidian-microblog) | `microblog-publish-plugin` | Publish notes to Micro.blog |
| [MIDI Logger](https://github.com/maybe-hello-world/midi-logger) | `midi-logger` | Insert parsed musical notes from MIDI input devices. |
| [Min Width](https://github.com/doitian/obsidian-min-width) | `obsidian-min-width` | Set the Minimum Width of the Active Pane in Obsidian |
| [Min3ditorHotkeys](https://github.com/d-sauer/Obsidian-Min3ditorHotkeys-plugin) | `obsidian-min3ditorhotkeys-plugin` | Additional editor hotkeys inspired by coding editors |
| [Mind Map](https://github.com/lynchjames/obsidian-mind-map) | `obsidian-mind-map` | A plugin to preview notes as Markmap mind maps |
| [Mindmap](https://github.com/OneCalmCloud/obsidian-mindmap) | `mindmap` | Create notes with Mindmaps. |
| [Mindmap NextGen](https://github.com/james-tindal/obsidian-mindmap-nextgen) | `obsidian-mindmap-nextgen` | View your Markdown as a mindmap |
| [Mini Toolbar](https://github.com/Quorafind/Obsidian-Mini-Toolbar) | `mini-toolbar` | mini context toolbar in editor |
| [Mini Vimrc](https://github.com/cabra-arretado/mini-vimrc-obsidian) | `mini-vimrc` | Set Vim keybiddings via .vimrc file. |
| [Mini-Rag](https://github.com/jjwheatley/mini-rag) | `mini-rag` | Leverage Retrieval Augmented Generation (RAG) for your Obsidian notes, using a locally running LLM or AI. |
| [Minidoro](https://github.com/ShaktiSampadSwain/minidoro) | `minidoro` | A minimal Pomodoro timer to help you focus. |
| [Minimal Quiz](https://github.com/Lutu-gl/Obsidian-Minimal-Quiz) | `minimal-quiz` | A minimalistic quiz plugin for Obsidian. Questions are defined in Markdown files with simple formatting. |
| [Minimal Theme Settings](https://github.com/kepano/obsidian-minimal-settings) | `obsidian-minimal-settings` | Change the colors, fonts and features of Minimal Theme. |
| [Minimize on Close](https://github.com/alberti42/obsidian-minimize-on-close) | `minimize-on-close` | Minimizes the app window to an icon after closing the last open pane |
| [Minio Uploader](https://github.com/seebin/obsidian-minio-uploader-plugin) | `minio-uploader` | Upload images, videos, audio, pdf, and other files to Minio OSS. |
| [Minitabs](https://github.com/ssjy1919/Obsidian-minitabs) | `minitabs` | Customize a set of nested tabs through code blocks. |
| [Minote Sync](https://github.com/emac/obsidian-minote-plugin) | `minote-sync` | Sync Minote(小米笔记) into your vault. |
| [Missing Link File Creator](https://github.com/Lemon695/obsidian-missing-link-file-creator) | `missing-link-file-creator` | Creates missing linked files and detects missing wiki links. |
| [Misskey Connector](https://github.com/minimarimo3/Obsidian-plugin-for-Misskey) | `misskey-connector` | Enables posting and embedding Misskey notes. |
| [Mixa](https://github.com/mixasite/obsidian-mixa) | `mixa` | Publish your notes and blog posts with Mixa directly from Obsidian |
| [MLIR Syntax Highlight](https://github.com/Lewuathe/obsidian-mlir-syntax-highlight) | `mlir-syntax-highlight` | Show syntax highlighing for MLIR in code blocks the editor |
| [Mobile Sidebar Notes](https://github.com/ckep1/obsidian-mobile-sidebar-notes) | `mobile-sidebar-notes` | Open notes & new tabs in the sidebar in the mobile app. |
| [MOC Link Helper](https://github.com/BogdanCodreanu/obsidian-moc-link-helper) | `moc-link-helper` | Helps with some MOC janitor-linking tasks. |
| [Mochi Cards Exporter](https://github.com/kalibetre/mochi-cards-exporter) | `mochi-cards-exporter` | Export Markdown notes to Mochi cards from within obsidian |
| [Mochi Cards Pro](https://github.com/xHayden/obsidian-mochi-cards-pro) | `mochi-cards-pro` | Create flashcards on Mochi.cards using the API provided by Mochi's Pro subscription. |
| [Modal forms](https://github.com/danielo515/obsidian-modal-form) | `modalforms` | Define forms for filling data that you will be able to open from anywhere you can run JS |
| [Modal Opener](https://github.com/likemuuxi/obsidian-modal-opener) | `modal-opener` | Open files and links in modal windows, or create and edit compatible files in modal windows. |
| [Mode manager](https://github.com/dk949/obsidian-mode-manager) | `mode-manager` | Provide an easier way to manipulate reading/editing and preview/source mode |
| [Model Viewer](https://github.com/janispritzkau/obsidian-model-viewer) | `model-viewer` | View and embed interactive 3D models directly in your vault, powered by Google's <model-viewer> component. Supports the glTF and GLB file formats. |
| [Modules](https://github.com/polyipseity/obsidian-modules) | `modules` | Load JavaScript and related languages like TypeScript modules from the vault and the Internet. |
| [Monokakido Copilot](https://github.com/NoHeartPen/obsidian-monokakido-copilot-plugin) | `monokakido-copilot` | During editing, simply double-press the option key to search with the Dictionaries by Monokakido. |
| [Mononote](https://github.com/czottmann/obsidian-mononote) | `mononote` | Ensures each note occupies only one tab. If a note is already open, its existing tab will be focussed instead of opening the same file in the current tab. |
| [Mood Tracker](https://github.com/dartungar/obsidian-mood-tracker) | `mood-tracker` | Track your moods & emotions easily. Visualize tracked history and browse the past entries. |
| [Moon server publisher](https://github.com/Dzoukr/MoonServerObsidianPlugin) | `moon-server-publisher` | Publish your notes directly to Moon server instance. |
| [MoreDraw](https://github.com/webceoboy/moredraw-obsidian) | `moredraw` | A infinite canvas whiteboard with ai to draw flowchart, mind map and other diagram. |
| [Morgen Tasks](https://github.com/morgen-so/morgen-obsidian) | `morgen-tasks` | Plan, time block, and track tasks from your vault in any calendar using Morgen. |
| [MostUsed](https://github.com/levi-ivel/MostUsed) | `most-used` | Creates a top 100 of the most used words in your notes |
| [Moulinette Search for TTRPG](https://github.com/SvenWerlen/moulinette-obsidian-plugin) | `moulinette` | Search, browse and download TTRPG (tabletop role-playing game) content from Moulinette Cloud. |
| [Mouse Navigation](https://github.com/HoBeom/obsidian-mouse-navigation) | `mouse-navigation` | Enables smooth navigation using mouse gestures for scrolling and switching pages. |
| [Mousewheel Image zoom](https://github.com/nicojeske/mousewheel-image-zoom) | `mousewheel-image-zoom` | This plugin enables you to increase/decrease the size of an image by scrolling |
| [Move Cursor On Startup](https://github.com/Treadder/move-cursor-on-startup) | `move-cursor-on-startup` | Move cursor right then left briefly on startup --> first opened note. Makes DataView expressions 'activate' automatically instead of waiting for user interaction. |
| [Move Files](https://github.com/nitishkhurana/obsidian-move-files-plugin) | `move-files` | Moves all the files linked to a open md file to a folder and updates the link in md file. |
| [Movie](https://github.com/onuraycicek/obsidian-movie) | `movie-obsidian` | Search for movies and trailers. |
| [Movie and TV show tracker](https://github.com/Shreshth-mehra/Obsidian-TV-Tracker) | `tv-tracker` | A Movie and TV show tracker. |
| [Movie Search](https://github.com/Gubchik123/obsidian-movie-search-plugin) | `movie-search` | Helps you find movies and create notes. |
| [Moviegrabber](https://github.com/Superschnizel/Obsidian-Moviegrabber) | `moviegrabber` | Grab movie data from public APIs and transform it into notes with a powerful templating engine. |
| [MP Preview](https://github.com/Yeban8090/mp-preview) | `mp-preview` | Preview and convert Markdown files to MP format |
| [mpv links](https://github.com/patsh90/mpv-obsidian-plugin) | `mpv-links` | Add mpv links with timestamps |
| [MrDoc](https://github.com/zmister2016/obsidian-mrdoc) | `mrdoc` | Synchronize documents between your vault and MrDoc. |
| [MSG Handler](https://github.com/ozntel/obsidian-msg-handler) | `msg-handler` | Easily display and search MSG files from Outlook in your Obsidian Vault |
| [MTG Card Links](https://github.com/aedans/mtg-card-links) | `mtg-card-links` | Link to Magic: the Gathering cards by enclosing the card name in square brackets. |
| [Multi Properties](https://github.com/technohiker/obsidian-multi-properties) | `multi-properties` | Adds Properties to multiple notes at once.  Either right-click a folder, or select multiple notes and right-click the selection. |
| [Multi State CheckBox Switcher](https://github.com/KubaMiszcz/MultiStateCheckBoxSwitcher) | `multi-state-checkbox-switcher` | Handle with multistate checkboxes. |
| [Multi Tag](https://github.com/technohiker/obsidian-multi-tag) | `multi-tag` | Adds a tag to multiple notes at once.  Either right-click a folder, or select multiple notes and right-click the selection. |
| [Multi-Column Markdown](https://github.com/ckRobinson/multi-column-markdown) | `multi-column-markdown` | This plugin adds functionality to create markdown documents with multiple columns of content viewable within Obsidian's preview mode |
| [Multi-line Formatting](https://github.com/nmady/obsidian-multi-line-formatting) | `multi-line-formatting` | Apply formatting to selected text, dealing with the paragraph breaks. |
| [Multilingual](https://github.com/leolazou/obsidian-multilingual) | `multilingual` | Simplify linking notes across multiple languages by automatically adding translations of note names into aliases. Designed for multilingual users. |
| [Multiplatform Highlights Importer](https://github.com/wwwkieran/obsidian-multiplatform-highlights-import) | `multiplatform-highlights-import` | Import and consolidate highlights from different reading sources. Supports reconciling books across reading sources. |
| [Multiple Daily Notes](https://github.com/vaibzzz123/multiple-daily-notes) | `multiple-daily-notes` | Create multiple daily notes in one vault, with additional configuration options including time offsets for creating notes past midnight, choosing the ribbon icon to use for the note, and more. |
| [Multiple Notes Outline](https://github.com/iiz00/obsidian-multiple-notes-outline) | `multiple-notes-outline` | Add custom views which show outlines of multiple notes with headings, links, tags and list items. |
| [Musical Text](https://github.com/tynanpurdy/musical-text) | `musical-text-highlighter` | Color codes sentences by length to visualize prose rhythm |
| [Mxmind Mindmap](https://github.com/webceoboy/mxmind-obsidian) | `mxmind` | Convert Markdown files to a mind map, mind map editor. export to image or pdf. |
| [my anime list text exporter](https://github.com/Xmoncoco/my_anime_list_text_exporter) | `my_anime_list_text_exporter` | add anime data for your notes |
| [My Bible](https://github.com/GsLogiMaker/my-bible-obsidian-plugin) | `gslogimaker-my-bible` | Your own customizable markdown bible for your personal vault! |
| [My SVGs](https://github.com/ce-omarbadawy/obsidian-my-svgs) | `my-svgs` | Registers your own SVGs into the global icon library for use with other plugins or however you want. |
| [My Thesaurus](https://github.com/Mara-Li/obsidian-my-thesaurus) | `my-thesaurus` | Automagically adds tags based on a simple csv file or a Markdown table. |
| [My Typewriter Line](https://github.com/dmo-code/MyTypewriterLine) | `my-typewriter-line` | Keep the active line in focus with customizable top and bottom scroll padding for typewriter-like editing. |
| [MySnippets](https://github.com/chetachiezikeuzor/MySnippets-Plugin) | `mysnippets-plugin` | MySnippets is a plugin that adds a status bar menu allowing the user to quickly toggle their snippets on and off 🖌. |
| [Natural Language Dates](https://github.com/argenos/nldates-obsidian) | `nldates-obsidian` | Create date-links based on natural language |
| [Natural Language Syntax Highlighting](https://github.com/artisticat1/nl-syntax-highlighting) | `nl-syntax-highlighting` | Highlight adjectives, nouns, adverbs, verbs, and conjunctions in the editor |
| [Nav Link Header](https://github.com/ahts4962/nav-link-header) | `nav-link-header` | Display navigation links at the top of the notes. |
| [Nav Weight](https://github.com/shu307/obsidian-nav-weight) | `nav-weight` | Sort your navigation items by Markdown frontmatter. |
| [Navigate Cursor History](https://github.com/heycalmdown/navigate-cursor-history) | `heycalmdown-navigate-cursor-history` | This plugin remembers the recent 50 cursor positions history and allows you to jump to them back and forth like VSCode |
| [Negative Heading](https://github.com/cyne-wulf/obsidian-negative-heading) | `negative-heading` | Render Discord-style "-#" lines as compact headings in reading view and the editor. |
| [Neighbouring Files](https://github.com/FabianUntermoser/obsidian-neighbouring-files-plugin) | `neighbouring-files` | Navigate to the next and previous file in the current directory |
| [Neo4j Graph View](https://github.com/HEmile/obsidian-neo4j-graph-view) | `neo4j-graph-view` | An Obsidian plugin for advanced graph visualization and querying using Neo4j. |
| [NerdFont Icon Picker](https://github.com/xavwe/obsidian-nerdfont-icon-picker) | `nerdfont-icon-picker` | Search and insert nerdfont icons. |
| [Nested Daily Todos](https://github.com/thomasbrezinski/obsidian-nested-daily-todos) | `nested-daily-todos` | Carry over incomplete todos from Daily Notes grouped by headers, with support for nesting and flexible todo states. |
| [Nested tags graph](https://github.com/drPilman/obsidian-graph-nested-tags) | `graph-nested-tags` | Links nested tags in graph view |
| [NetClip](https://github.com/hariiy-sys/Obsidian-NetClip) | `net-clip` | Clip, save, search, and browse web pages within your vault |
| [Netwik](https://github.com/fivol/netwik-obsidian) | `netwik` | This plugin provides access to global network of notes. Anyone can create, view or edit notes. All changes will be synchronized between all participants |
| [NeuroVox](https://github.com/Synaptic-Labs-AI/NeuroVox) | `neurovox` | Enhances your note-taking with voice transcription and AI capabilities |
| [New 3D Graph](https://github.com/Apoo711/obsidian-3d-graph) | `new-3d-graph` | Visualize your vault in 3D with a powerful, highly customizable, and filterable graph. |
| [New Bullet With Time](https://github.com/Quorafind/Obsidian-New-Bullet-With-Time) | `obsidian-new-bullet-with-time` | Allows you to auto add current time to new bullet line. |
| [New Filename](https://github.com/TheLoneWanderer4/obsidian-uuid-title) | `new-file-name` | Change the default filename used for new notes |
| [New Note Fixer](https://github.com/mnaoumov/obsidian-new-note-fixer) | `new-note-fixer` | Unifies the way non-existing notes are created when clicking on their links. |
| [New Note New Window](https://github.com/Pr0dt0s/new-note-new-window) | `obsidian-new-note-new-window` | Plugin for easily opening new notes in a floating window. |
| [New Tab +](https://github.com/Raphlette/obsidian-new-tab-plus) | `new-tab-plus` | Allow to open Markdown files, graphs, canvases, images, audio, video, and PDFs in a new tab by default. |
| [newslog](https://github.com/protoavatar/obsidian-newsletters) | `newslog` | Sync newsletters and kindle highlights from your newslog.me daily bundles. |
| [Next Link](https://github.com/jdluque/next-link) | `next-link` | Jump quickly between note links. |
| [Next TOC](https://github.com/Raven-Pensieve/obsidian-next-toc) | `next-toc` | Floating panel displaying the current document's reading progress, table of contents, and navigation aids. |
| [Nextcloud Link Fixer](https://github.com/KFreon/nextcloud-link-fixer) | `nextcloud-link-fixer` | Nextcloud breaks Wiki-links (used by Obsidian). This fixes them |
| [Nexus AI Chat Importer](https://github.com/Superkikim/nexus-ai-chat-importer) | `nexus-ai-chat-importer` | Import AI conversations from ChatGPT, Claude, and Le Chat exports into Obsidian. |
| [Nifty Links](https://github.com/x-Ai/obsidian-nifty-links) | `nifty-links` | Generate elegant, Notion-style rich link cards to enhance your note-taking experience |
| [Ninja Cursor](https://github.com/vrtmrz/ninja-cursor) | `ninja-cursor` | The plugin which enhance cursor visibility. |
| [No dupe leaves](https://github.com/scambier/obsidian-no-dupe-leaves) | `no-dupe-leaves` | Don't reopen notes that are already open |
| [No Empty Windows](https://github.com/popscallion/obsidian-no-empty-windows) | `no-empty-windows` | Closes Obsidian window with cmd+W on Mac when the last tab is closed. |
| [No more flickering inline math](https://github.com/RyotaUshio/obsidian-inline-math) | `inline-math` | Remove flickering inline math. |
| [Node Auto Resize](https://github.com/Quorafind/Obsidian-Node-Auto-Resize) | `node-auto-resize` | Automatically resize the node when the content changes. |
| [Node Factor](https://github.com/CalfMoon/node-factor) | `node-factor` | Customize factors effecting node size in graph. |
| [Node Screenshot](https://github.com/cestfredy/obsidian-canvas-node-screenshot) | `canvas-node-screenshot` | Capture node effortlessly with precision screenshot. |
| [NodeFlow](https://github.com/LincZero/obsidian-node-flow) | `node-flow` | Render node streams like `ComfyUi`, `UE`, `Houdini`, `Blender`, etc., to make it easy to write relevant notes. json describes the chart, compared to screenshots, making it easier to modify later. The plugin is also compatible with blogs. |
| [Nomnoml Diagram](https://github.com/Daeik/obsidian-nomnoml-diagram) | `obsidian-nomnoml-diagram` | Draw nomnoml diagrams in Obsidian notes |
| [Noor](https://github.com/MKSherbini/obsidian-noor) | `noor` | Aims to help Muslims stay enlightened with Islam, Quran, Hadith, and Sunnah |
| [Nostr Writer](https://github.com/jamesmagoo/nostr-writer) | `nostr-writer` | Publish your writing directly to Nostr. |
| [Note 2 Tag Generator](https://github.com/augustin7698/note-2-tag-generator) | `note-2-tag-generator` | Generate tags from notes without openai key in multiple languages |
| [Note aliases](https://github.com/pulsovi/obsidian-note-aliases) | `note-aliases` | This plugin manage aliases of notes in Obsidian. |
| [Note archiver](https://github.com/thenomadlad/obsidian-note-archiver) | `note-archiver` | Tools to archive your notes in another folder |
| [Note Auto Creator](https://github.com/SimonTC/obsidian-note-autocreation) | `obsidian-note-autocreator` | Automatically create notes when links are created to them. |
| [Note Batcher](https://github.com/MrAnyx/obsidian-note-batcher) | `note-batcher` | Create all unresolvered links with a single click on your Obsidian vault |
| [Note Chain](https://github.com/zigholding/obsidian-notechain-plugin) | `note-chain` | File sorting and hierarchical indentation display in the File Explorer. MCP Server, easyapi, and more. |
| [Note Codes](https://github.com/SilverEzhik/obsidian-note-codes) | `note-codes` | Reference your notes from anywhere with simple 4-character codes. |
| [Note Companion (prev. File Organizer 2000)](https://github.com/Nexus-JPF/note-companion) | `fileorganizer2000` | AI-powered note organization and chat. Requires subscription or self-hosting with your own API keys. |
| [Note Companion Folder](https://github.com/vkodocha/NoteCompanionFolder) | `note-companion-folder` | Manage a separate folder of attachments for each note. |
| [Note Content Pusher](https://github.com/lizard-heart/obsidian-note-content-pusher) | `obsidian-note-content-pusher` | An Obsidian plugin to automatically create notes with some specified content when you link to a note that doesn't yet exist. |
| [Note Definitions](https://github.com/dominiclet/obsidian-note-definitions) | `note-definitions` | Personal dictionary for your notes |
| [Note Favicon](https://github.com/mdklab/note-favicon) | `note-favicon` | Extracts a URL from the frontmatter of notes and displays an associated favicon image next to the note title in the file tree. Supports standard URLs and base64-encoded images. |
| [Note Folder Autorename](https://github.com/pjeby/note-folder-autorename) | `note-folder-autorename` | Turn notes into folders and automaticaly move/rename their folders when they move or are renamed. |
| [Note From Form](https://github.com/ArhiChief/obsidian-note-from-form) | `note-from-form` | Define dynamic input form and use it to create notes |
| [Note Gallery](https://github.com/pashashocky/obsidian-note-gallery) | `note-gallery` | A masonry gallery view for your notes. Allows to have a birds eye view over the notes in your vault. |
| [Note ID](https://github.com/dominikmayer/obsidian-note-id) | `note-id` | Displays notes by their ID, enabling structured sequences for manuscripts or Zettelkasten ("Folgezettel"). |
| [Note Linker](https://github.com/AlexW00/obsidian-note-linker) | `obisidian-note-linker` | Automatically find and link notes in Obsidian |
| [Note Linker with Previewer](https://github.com/nickrallison/obsidian-note-linker-with-previewer) | `note-linker-with-previewer` | Link your notes together |
| [Note Locker](https://github.com/Felvesthe/Note-Locker) | `note-locker` | Lock notes to open in preview mode by default. |
| [Note Minimap](https://github.com/YairSegel/ObsidianMinimap) | `minimap` | Add a minimap to your Markdown notes. |
| [Note Navigator](https://github.com/mudnug/note-navigator) | `note-navigator` | Streamlines note review by automatically navigating to the next note upon deletion. Adds commands to go to the previous and next note, respecting user-selected sort order. |
| [Note Placeholder](https://github.com/XZSt4nce/note-placeholder) | `note-placeholder` | Replaces text of note link to placeholder in view mode. |
| [Note Refactor](https://github.com/lynchjames/note-refactor-obsidian) | `note-refactor-obsidian` | Extract note content into new notes and split notes |
| [Note Reviewer](https://github.com/TravisLinkey/note-reviewer) | `note-reviewer` | Help knowledge retention by reviewing and filtering notes. |
| [Note Splitter](https://github.com/decaf-dev/obsidian-note-splitter) | `note-splitter` | Split a note into individual notes based on a delimiter. |
| [Note Status](https://github.com/devonthesofa/obsidian-note-status) | `note-status` | Track and change note statuses across your vault with templates, bulk folder actions, dashboards, and non-Markdown support. |
| [Note Sync](https://github.com/zigholding/obsidian-notesync-plugin) | `note-sync` | Sync notes or plugins between vaults. |
| [Note Synchronizer](https://github.com/tansongchen/obsidian-note-synchronizer) | `note-synchronizer` | This is a plugin for synchornizing Obsidian notes to other note-based softwares like Anki, following more strictly the principles of Zettelkasten and treating each Obsidian file as a note. |
| [Note to RED](https://github.com/Yeban8090/note-to-red) | `note-to-red` | Convert Markdown notes to RED (Xiaohongshu) style images |
| [Note Toolbar](https://github.com/chrisgurney/obsidian-note-toolbar) | `note-toolbar` | Add customizable toolbars to your notes. |
| [Note UID Generator](https://github.com/Netajam/obsidian_note_uid_generator) | `note_uid_generator` | Automatically or manually generates Unique IDs (UUID, NanoID, or ULID) for notes and registers them in metadata (frontmatter). |
| [Notebook Navigator](https://github.com/johansan/notebook-navigator) | `notebook-navigator` | Replace the default file explorer with a clean two-pane interface featuring folder tree, tag browsing, file previews, keyboard navigation, drag-and-drop, pinned notes, and customizable display options. |
| [Notemd](https://github.com/Jacobinwwey/obsidian-NotEMD) | `notemd` | Enhances notes using LLMs: 1) Processes text to add [[wiki-links]] and create concept notes. 2) Performs web research (Tavily/DuckDuckGo) and summarizes topics. 3) Generates content from note titles. 4) Translates notes/selections. 5) build powerful knowledge graphs Supports multiple LLM providers and customizable output. |
| [NoteMover shortcut](https://github.com/bueckerlars/obsidian-note-mover-shortcut) | `note-mover-shortcut` | Quickly and easily move notes to a predefined folder. Perfect for organizing your notes. |
| [NotePix](https://github.com/AyushParkara/NotePix) | `notepix` | Automatically uploads images to your public or private GitHub repository, replacing local links with the corresponding remote URLs |
| [Notes 2 Tweets](https://github.com/Tej-Sharma/notes2tweets-obsidian) | `notes2tweets` | Generate and schedule tweets automatically from your notes |
| [Notes dater](https://github.com/PaulTreanor/notes-dater) | `notes-dater` | Adds created on and last updated on dates of the active note to the status bar. |
| [Notes Explorer](https://github.com/tu2-atmanand/obsidian-notes-explorer) | `notes-explorer` | View all your notes in a form of cards for better visual navigation and revision of your notes. |
| [Notes Merger](https://github.com/niffka/notes-merger) | `notes-merger` | Merge notes into a single markdown document based on index Markdown file. |
| [Notes Refresher](https://github.com/connorpark24/refresher-plugin) | `notes-refresher` | Provides AI-generated summaries (GPT) of three notes from your Vault every day. |
| [Notes Sync Share](https://github.com/Alt-er/obsidian-sync-share) | `notes-sync-share` | Sync and share (publish) your notes in your own private service. |
| [NoteSmith](https://github.com/csteamengine/notesmith) | `notesmith` | NoteSmith is a powerful note-refining plugin using OpenAI's API. It allows you to refine your notes, generate summaries, and create new content based on your existing notes. |
| [NotesOn Publish](https://github.com/shapkinaa/noteson-obsidian-plugin) | `noteson-publish` | Make single notes instantly available on the web. |
| [NoteToMP](https://github.com/sunbooshi/note-to-mp) | `note-to-mp` | Send notes to WeChat MP drafts, or copy notes to WeChat MP editor, perfect preservation of note styles, support code highlighting, line numbers in code, and support local image uploads. |
| [NoteTweet🐦](https://github.com/chhoumann/notetweet_obsidian) | `notetweet` | This plugin allows you to post tweets directly from Obsidian. |
| [Notice logger](https://github.com/gapmiss/notice-logger) | `notice-logger` | Logs all notices to the developer console, with optional prefix and timestamp. |
| [Notification Controller](https://github.com/juan-miii/obsidian-notice-plugin) | `notice-controller` | Manages notifications at startup. |
| [Notion Video](https://github.com/LastKnightCoder/obsidian-notion-video) | `obsidian-notion-video` | embed your notion video in obsidian |
| [Nova](https://github.com/shawnduggan/nova) | `nova` | Your AI writing partner that edits exactly where you want - select text and transform, or chat at cursor position. |
| [Novel word count](https://github.com/isaaclyman/novel-word-count-obsidian) | `novel-word-count` | Displays a word count (and more!) for each file, folder and vault in the File Explorer pane. |
| [NovelAI](https://github.com/SalokinGreen/NAI4Obsidian) | `nai4obsidian` | Generate text with NovelAI's models. |
| [NSFW filter](https://github.com/catvatar/Obsidian-NSFW-Plugin) | `nsfw-filter` | Adds customizable and easly togglable NSFW filter |
| [Nuke Orphans](https://github.com/sandorex/nuke-orphans-plugin) | `nuke-orphans` | Plugin that trashes orphaned files and attachments |
| [Number Headings](https://github.com/onlyafly/number-headings-obsidian) | `number-headings-obsidian` | Automatically number or re-number headings in an Obsidian document |
| [Numerals](https://github.com/gtg922r/obsidian-numerals) | `numerals` | Numerals turns any code block into an advanced calculator. Evaluates math expressions on each line of a code block, including units, currency, and optional TeX rendering. |
| [Nutstore Sync](https://github.com/nutstore/obsidian-nutstore-sync) | `nutstore-sync` | Sync your vault with Nutstore/坚果云 using WebDAV protocol. |
| [NyanBar](https://github.com/xhyabunny/nyanbar) | `nyanbar` | Nyan Cat Progress Bar generator! |
| [O2](https://github.com/songkg7/o2) | `o2` | This is a plugin to make obsidian markdown syntax compatible with other markdown syntax. |
| [Object Oriented Thinking](https://github.com/TiagoJacinto/obsidian-object-oriented-thinking) | `object-oriented-thinking` | Add inheritance-like behavior to notes. |
| [Object Writer](https://github.com/IagoGrah/obsidian-object-writer) | `object-writer` | Quickly create a note with a prompt for object writing. |
| [Obligator](https://github.com/Newbrict/obsidian-obligator) | `obligator` | A fully featured replacement for the built-in daily notes plugin. Obligator functions like a virtual bullet journal by copying over unchecked to-do items to your new daily note, along with adding any scheduled items you've set up |
| [Obsidian Anki Sync](https://github.com/debanjandhar12/Obsidian-Anki-Sync) | `ObsidianAnkiSync` | Obsidian plugin to make flashcards and sync them to Anki. |
| [Obsidian Attendance](https://github.com/Tiim/obsidian-attendance) | `obsidian-attendance` | This plugin helps you track attendance. |
| [Obsidian Badge](https://github.com/linjunpop/obsidian-badge) | `obsidian-badge` | This is a plugin to show badge for Obsidian. |
| [Obsidian Chevereto Image Uploader](https://github.com/kkzzhizhou/obsidian-chevereto-image-uploader) | `obsidian-chevereto-image-uploader` | This plugin uploads the image in your clipboard to chevereto automatically when pasting. |
| [obsidian echarts](https://github.com/cumany/obsidian-echarts) | `obsidian-echarts` | obsidian echarts |
| [Obsidian Functionplot](https://github.com/leonhma/obsidian-functionplot) | `obsidian-functionplot` | A plugin for displaying mathematical graphs in obsidian.md. |
| [Obsidian Graphviz](https://github.com/QAMichaelPeng/obsidian-graphviz) | `obsidian-graphviz` | Render Graphviz Diagrams |
| [Obsidian matrix](https://github.com/MohrJonas/obsidian-matrix) | `obsidian-matrix` | Utility to easily create LaTeX matrices |
| [Obsidian MtG](https://github.com/omardelarosa/obsidian-mtg) | `obsidian-mtg` | A plugin for managing Magic: The Gathering decks and card lists as Obsidian notes |
| [Obsidian OCR](https://github.com/MohrJonas/obsidian-ocr) | `obsidian-ocr` | Add ocr capabilities to obsidian |
| [Obsidian Query Language](https://github.com/jplattel/obsidian-query-language) | `obsidian-query-language` | This plugin allows you to query notes and represent data within Obsidian |
| [Obsidian shared to Notion](https://github.com/EasyChris/obsidian-to-notion) | `obsidian-to-notion` | This is a  plugin for Obsidian. This plugin share obsidian md  file to notion with notion api |
| [Obsidian Stylist](https://github.com/ixth/obsidian-stylist) | `obsidian-stylist` | Obsidian plugin that allows to add classes and styles on markdown blocks |
| [Obsidian Temple](https://github.com/garyng/obsidian-temple) | `obsidian-temple` | A plugin for templating in Obsidian, powered by Nunjucks. |
| [obsidian-dataset-aid](https://github.com/connerohnesorge/Text-Dataset-Aid-Plugin) | `obsidian-dataset-aid` |  |
| [obsidian-title-index](https://github.com/renmu123/obsidian-markdown-index) | `obsidian-title-index` | obsidian-title-index |
| [Obsidian_to_Anki](https://github.com/ObsidianToAnki/Obsidian_to_Anki) | `obsidian-to-anki-plugin` | This is an Anki integration plugin! Designed for efficient bulk exporting. |
| [ObsidianTweaks](https://github.com/JeppeKlitgaard/ObsidianTweaks) | `obsidian-tweaks` | Adds some convenient tweaks including improved toggling and ergonomic commands |
| [Obsidiosaurus](https://github.com/CIMSTA/obsidiosaurus) | `obsidiosaurus` | Connect your vault to Docusaurus |
| [ObsiDOOM](https://github.com/twibiral/ObsiDOOM) | `obsidoom` | Play DOOM and many other retro games in your Obsidian app. You can also play Prince of Persia, Mortal Combat, GTA, Sim City, and Need for Speed. |
| [Obsifetch](https://github.com/tabibyte/obsifetch) | `obsifetch` | A neofetch-style vault information display |
| [Obsimian Exporter](https://github.com/motif-software/obsimian) | `obsimian-exporter` | Exports data from Obsidian APIs, feeding the Obsimian simulation framework for testing plugins. |
| [Obsius Publish](https://github.com/jonstodle/obsius-obsidian-plugin) | `obsius-publish` | Make single notes instantly available on the web. |
| [Occura](https://github.com/Krusty84/obsidian-occura-plugin) | `occura-word-highlighter` | Find and highlight all occurrences of selected text in notes, similar to Notepad++ or IDEs. |
| [OCR Extractor](https://github.com/jritzi/ocr-extractor) | `ocr-extractor` | Extract text from documents, images, etc. and store it as Markdown in your notes. |
| [OCR-AI](https://github.com/L3-N0X/obsidian-marker) | `marker-api` | Convert PDFs to beautiful rich Markdown notes with tables, images, formulas and OCR. Works with self-hosted Marker API and free Mistral OCR API! |
| [Old Note Admonitor](https://github.com/tadashi-aikawa/obsidian-old-note-admonitor) | `obsidian-old-note-admonitor` | This Obsidian plugin shows warnings if the note has not been updated in the last specific days |
| [Ollama](https://github.com/hinterdupfinger/obsidian-ollama) | `ollama` | This is a plugin for Obsidian that enables the usage of Ollama within your notes. |
| [Ollama Chat](https://github.com/brumik/obsidian-ollama-chat) | `ollama-chat` | Chat with your notes with the help of Ollama. |
| [OMG.lol Publisher](https://github.com/ericmwalk/obsidian-omglol-publisher) | `statuslol-post` | Allows you to post to weblogs.lol, status.lol, some.pics and paste.lol. |
| [Omg.publish](https://github.com/MayMeow/obsidian-omglol-statuslog) | `omglol-statuslog-publish` | Publish selected text to omg.lol service. |
| [Omnisearch](https://github.com/scambier/obsidian-omnisearch) | `omnisearch` | A search engine that just works |
| [Omnivore](https://github.com/omnivore-app/obsidian-omnivore) | `obsidian-omnivore` | This is an Omnivore plugin for Obsidian. |
| [On This Day](https://github.com/jose-elias-alvarez/obsidian-on-this-day) | `on-this-day` | Show your daily notes from this day in a simple panel view. |
| [On This Day I](https://github.com/benstuart0/on-this-day-i-obsidian) | `on-this-day-i` | AI tools for Daily Journals |
| [One Step Wiki Link](https://github.com/busyoGG/OneStepWikiLink) | `one-step-wiki-link` | 一步添加 wiki 链接 |
| [OnlyWorlds Builder](https://github.com/OnlyWorlds/obsidian-plugin) | `onlyworlds-builder` | World building structure with OnlyWorlds integration |
| [Onto Tracker](https://github.com/jdchart/onto-tracker) | `onto-tracker` | Manage projects according to an ontology. |
| [Onyx Boox Annotation & Highlight Extractor](https://github.com/akosbalasko/Onyx-Boox-Annotation-Highlight-Extractor) | `onyx-boox-extractor` | This plugin extracts annotations and highlights files exported from Onyx Boox tablets, and converts them to reference, literature and permanent notes fitting to the Zettelkasten method. |
| [Open cards in imdone](https://github.com/imdone/imdone-obsidian-plugin) | `imdone-obsidian-plugin` | This plugin allows imdone users to open their imdone board from a document in their obsidian vault that contains imdone cards. |
| [Open Editors](https://github.com/4Source/open-editors-obsidian-plugin) | `open-editors` | Adds a view which shows the opened windows, groups, tabs and editors inside them. Makes managing the open editors easier. |
| [Open File by Magic Date](https://github.com/SimplGy/obsidian-open-file-by-magic-date) | `obsidian-open-file-by-magic-date` | Define a Moment.js date pattern that specifies the file that is most important to you (eg: your daily/weekly/monthly note). Will create the file if it doesn't exist. |
| [Open files with commands](https://github.com/LostPaul/ob-open-files-with-commands) | `open-files-with-commands` | Create commands that only open one file at the time and that can be used with the commander plugin. |
| [Open Gate](https://github.com/nguyenvanduocit/obsidian-open-gate) | `open-gate` | Embed any website to Obsidian, you have anything you need in one place. You can browse website and take notes at the same time. e.g. Ask ChatGPT and copy the answer directly to your note. |
| [Open in Cursor](https://github.com/awaken233/open-in-cursor) | `open-in-cursor` | Open current file in Cursor/VSCode/Kiro with per-command hotkeys and cursor-position jump |
| [Open in GitHub](https://github.com/Hacker-C/obsidian-open-in-github-plugin) | `open-in-github` | Open the current project or file in github.com. |
| [Open In New Tab](https://github.com/patleeman/obsidian-open-in-new-tab) | `open-in-new-tab` | Opens files in new tabs |
| [Open in other editor](https://github.com/yekingyan/obsidian-open-in-other-editor) | `obsidian-open-in-other-editor` | Open current active file in gVim or VScode. |
| [Open in Terminal](https://github.com/Feng6611/Obsidian-open-in-Teminal) | `open-in-terminal` | Open your vault in a new terminal window, launch CLI tools, or run quick Git commands from Obsidian. |
| [Open Interpreter](https://github.com/MikeBirdTech/obsidian-open-interpreter) | `open-interpreter` | Use Open Interpreter to run automatic operations on your vault |
| [Open Link With](https://github.com/MamoruDS/obsidian-open-link-with) | `obsidian-open-link-with` | Open external link with specific browser / in-app view in Obsidian |
| [Open or Create File](https://github.com/iparips/open-or-create-file-obsidian-plugin) | `open-or-create-file-command` | Create custom commands that open or create files using configurable patterns and templates. |
| [Open Plugin Settings](https://github.com/Mara-Li/obsidian-open-settings) | `open-plugin-settings` | Create a command to open a specified plugin settings. |
| [Open Related Url](https://github.com/dpickett/open-related-url) | `open-related-url` | Opens URLs found in a note's YAML frontmatter |
| [Open Tab Settings](https://github.com/jesse-r-s-hines/obsidian-open-tab-settings) | `open-tab-settings` | Adds options to customize how tabs are opened, including open in new tab by default, preventing duplicate tabs, and more. |
| [Open vault in VS Code](https://github.com/NomarCub/obsidian-open-vscode) | `open-vscode` | Ribbon button, command and file explorer context menu to open the vault as a Visual Studio Code (VSCode) workspace |
| [Open with](https://github.com/phibr0/obsidian-open-with) | `open-with` | This Plugin allows you to add multiple other programs to open notes with. |
| [Open with Natural Language Dates](https://github.com/charliecm/obsidian-open-with-nldates) | `open-with-nldates` | Open a daily note using natural language. Requires "Natural Language Dates" plugin to work. |
| [open-as-md](https://github.com/kursad-k/obsidian-openasmd) | `open-as-md` | Edit non-md file types as markdown files |
| [OpenAPI Renderer](https://github.com/Ssentiago/obsidian-openapi-renderer) | `openapi-renderer` | Integrate OpenAPI specification management with features for version control, visualization, editing, and easy navigation of API specs. |
| [OpenAugi](https://github.com/bitsofchris/openaugi-obsidian-plugin) | `openaugi` | Process information faster with augmented intelligence (AI for thinkers). Parse your voice notes into atomic notes, tasks, and summaries. Grab context from dataview queries and linked notes. De-duplicate and merge atomic ideas into a clean, organized vault. |
| [Opener: New Tab by Default](https://github.com/lukemt/obsidian-opener) | `opener` | Open links in new tabs by default. If the note is already open in another tab, it switches to it. Can also open PDFs and other file formats in System Apps when cmd/ctrl is hold. |
| [OpenWeather](https://github.com/willasm/obsidian-open-weather) | `open-weather` | This plugin returns the current weather from OpenWeather in a configurable string format. |
| [OpenWords](https://github.com/insile/OpenWords) | `openwords` | 用于英语学习中背单词与单词管理的插件 |
| [Optimize Canvas Connections](https://github.com/felixchenier/obsidian-optimize-canvas-connections) | `optimize-canvas-connections` | An Obsidian plugin that declutters a canvas by reconnecting notes using their nearest edges. |
| [Order List](https://github.com/lizard-heart/obsidian-order-list-plugin) | `order-list` | Orders list by number at end of line |
| [Ordered List Style](https://github.com/erykwalder/obsidian-list-style) | `list-style` | Set ordered list style inline in Obsidian.md. Alphabetic lists, roman numeral lists, etc. |
| [Org Mode](https://github.com/ryanpcmcquen/obsidian-org-mode) | `obsidian-org-mode` | Add Org Mode support to Obsidian. |
| [Organized daily notes](https://github.com/duchangkim/organized-daily-notes) | `organized-daily-notes` | Automatically organizes your daily notes into customizable folder structures (Year/Month/Week) for enhanced organization and easier navigation |
| [Orgmode (cm6)](https://github.com/BBazard/obsidian-orgmode-cm6) | `orgmode-cm6` | Edit Orgmode files in Obsidian. |
| [Orion Publish](https://github.com/seanrcollings/orion-publish-plugin) | `orion-publish` | Quickly and easily publish your notes to the web with Orion Publish. |
| [Orthography](https://github.com/denisoed/obsidian-orthography) | `obsidian-orthography` | Check & fix orthography errors in text. |
| [Oura Ring](https://github.com/kinabalu/obsidian-oura-plugin) | `obsidian-oura-plugin` | A plugin for importing Oura Ring data from the Cloud-based API |
| [Outline Converter](https://github.com/masaki39/outline-converter) | `outline-converter` | Convert outline to continuous text. |
| [Outline to task list](https://github.com/alexandrerbb/obsidian-outline-tasklist-plugin) | `outline-task-list` | Convert a note's outline to a task list. |
| [Outline++](https://github.com/RyotaUshio/obsidian-outline-plus) | `outline-plus` | Fix issues of the built-in outline view & optionally render markdown in it. |
| [Outliner](https://github.com/vslinko/obsidian-outliner) | `obsidian-outliner` | Work with your lists like in Workflowy or RoamResearch. |
| [Outlook Meeting Notes](https://github.com/davidingerslev/outlook-meeting-notes) | `outlook-meeting-notes` | Creates meeting notes for Outlook appointments and meetings. |
| [Overdue](https://github.com/parente/obsidian-overdue) | `obsidian-overdue` | Marks items as [[Overdue]] if they are not checked off by their due date |
| [OZ Calendar](https://github.com/ozntel/oz-calendar) | `oz-calendar` | View your notes in Calendar using any YAML key with date |
| [OzanShare Publish](https://github.com/ozntel/ozanshare-publish-plugin) | `ozanshare-publish` | Publish your markdown notes with a single click from your vault. |
| [Packrat](https://github.com/therden/packrat) | `tasks-packrat-plugin` | Process completed recurring Tasks |
| [packUp4AI](https://github.com/shuxueshuxue/PackUp4AI) | `packup4ai` | Collect related notes based on links/backlinks to provide focused context for external AI chatbots. Explore note relationships visually and export the bundle. |
| [Page Heading From Links](https://github.com/beet/page-headings-obsidian-plugin) | `page-heading-from-links` | Inserts a heading into blank pages from the filename |
| [Page Properties](https://github.com/necauqua/obsidian-page-properties) | `page-properties` | Render page properties similar to Logseq |
| [Page Scroll](https://github.com/chenshutian9610/obsidian-pagescroll-plugin) | `page-scroll` | Page Up\|Down\|Top\|Bottom |
| [Painter](https://github.com/KraXen72/obsidian-painter) | `painter` | Paint text different colors |
| [Palta Note](https://github.com/mrniket/palta-obsidian-plugin) | `palta-note` | Render Bhatkhande notation for Tabla. |
| [Pandoc Extended Markdown](https://github.com/ErrorTzy/obsidian-pandoc-extended-markdown) | `pandoc-extended-markdown` | Render Pandoc extended markdown syntax: fancy lists, definition lists, example lists with cross-references, superscripts, and subscripts. |
| [Pandoc Plugin](https://github.com/OliverBalfour/obsidian-pandoc) | `obsidian-pandoc` | This is a Pandoc export plugin for Obsidian. It provides commands to export to formats like DOCX, ePub and PDF. |
| [Pandoc Reference List](https://github.com/obsidian-community/obsidian-pandoc-reference-list) | `obsidian-pandoc-reference-list` | Displays a formatted reference in the sidebar for each pandoc citekey present in the current document. |
| [Pane Relief](https://github.com/pjeby/pane-relief) | `pane-relief` | Per-tab history, hotkeys for pane/tab movement, navigation, sliding workspace, and more |
| [Paper Importer](https://github.com/chenzhekl/obsidian_paper_importer) | `paper_importer` | Import papers from arXiv with one click. |
| [Paperless](https://github.com/Talal-A/obsidian-paperless) | `paperless` | Link your paperless-ngx documents within your vault. |
| [Papers](https://github.com/willjhliang/obsidian-papers) | `papers` | Retrieve and import research papers. |
| [Papyrus](https://github.com/Papyrus-doc-ai/papyrus-obsidian) | `papyrus` | An AI powered documentation assistant |
| [PARA Shortcuts](https://github.com/gOATiful/para-shortcuts) | `para-shortcuts` | This plugin serves usefull commands to setup and manage your knowledge using the PARA method. |
| [PARA Workflower](https://github.com/trucke/para-workflower) | `para-workflower` | Helpful commands for starting and working in your vault with the PARA method. |
| [Party🎉](https://github.com/shap-po/obsidian-party) | `obsidian-party` | An implementation of party.js for Obsidian. Create confetti, sparkles and even custom effects in your notes! |
| [Password Audit](https://github.com/0xPrashanthSec/password-audit) | `password-audit` | Audit password strength, check breaches, and generate secure passwords. Not a password manager. |
| [Password Protect](https://github.com/Aspharmyx/obsidian-password-protect) | `password-protect` | Password protect your notes. |
| [Password Protection](https://github.com/qing3962/password-protection) | `password-protection` | Lock and protect your private notes and diary with a password, no encrypt, no decrypt. |
| [Paste as Embed](https://github.com/i-m-mll/obsidian-paste-as-embed) | `paste-as-embed` | Paste text into a separate note, and embed the note. |
| [Paste as file link](https://github.com/mbedded/obsidian-paste-file-link) | `paste-as-file-link` | Paste clipboard content as file links into existing notes, when a file with this name is existing. |
| [Paste As Html](https://github.com/maotong06/obsidian-paste-as-html-plugin) | `obsidian-paste-as-html` | Paste As Html, Keep the original css style. Paste from web browser |
| [Paste From History](https://github.com/Karakaz/obsidian-paste-from-history) | `paste-from-history` | Paste from the editor's recent clipboard history. |
| [Paste Image Into Property](https://github.com/Nitero/obsidian-paste-image-into-property) | `paste-image-into-property` | Paste images from the clipboard into frontmatter properties in live preview. |
| [Paste image Png to Jpeg](https://github.com/musug/obsidian-paste-png-to-jpeg) | `obsidian-paste-png-to-jpeg` | Screenshot png to jpeg and compress and rename |
| [Paste image rename](https://github.com/reorx/obsidian-paste-image-rename) | `obsidian-paste-image-rename` | Rename pasted images and all the other attchments added to the vault |
| [Paste Image Rename and Convert](https://github.com/Yiaos/obsidian-paste-image-rename-convert) | `paste-image-rename-convert` | Rename pasted images and convert them to webp or jpg |
| [Paste Link](https://github.com/jose-elias-alvarez/obsidian-paste-link) | `paste-link` | Intelligently paste Markdown links. |
| [Paste Mode](https://github.com/jglev/obsidian-paste-mode) | `obsidian-paste-to-current-indentation` | Paste content and mark block quotes at any level of indentation. |
| [Paste Quote](https://github.com/brokensandals/obsidian-paste-quote-plugin) | `paste-quote` | Helps with formatting and generating citations when pasting quotes from the clipboard. |
| [Paste Reformatter](https://github.com/keathmilligan/obsidian-paste-reformatter) | `paste-reformatter` | Reformat pasted text for precise control. |
| [Paste transform](https://github.com/rekby/obsidian-paste-transform) | `paste-transform` | Handle pasted text and and transform it by regexp rules. |
| [Paste URL into selection](https://github.com/denolehov/obsidian-url-into-selection) | `url-into-selection` | Paste URL "into" selected text to create markdown links. |
| [Pasterly](https://github.com/easternkite/Pasterly) | `pasterly` | Automatically upload clipboard images to Firebase Storage and insert them as markdown links. |
| [Path Finder](https://github.com/jerrywcy/obsidian-path-finder) | `obsidian-path-finder` | A plugin that can find the shortest path between two notes. Not sure who will want to use it... |
| [Path Title](https://github.com/jdeal/obsidian-path-title-plugin) | `obsidian-path-title` | Adds path (or optional replacement) to the filename title of each pane |
| [Pathfinder 2E Action Icons](https://github.com/thiagocoutinhor/pf2-action-icons) | `pf2-action-icons` | Displays Pathfinder 2E action icons easily |
| [PDF break page](https://github.com/corentin-godefroy/Obsidian-BreakPage) | `break-page` | Add shortkey and command to insert a break page formating for pdf exports. |
| [PDF Emojis](https://github.com/mmarusiak/pdf-emojis-plugin) | `pdf-emojis` | Helps you exporting all your emojis to pdf (even those in headings)! |
| [PDF Folder to Markdowns](https://github.com/crishood/pdf-folder-to-markdowns) | `pdf-folder-to-markdowns` | Convert a folder of PDFs into a folder of Markdown files with embedded PDFs. Ideal for users migrating PDF notes from apps like Boox or organizing reference materials inside Obsidian, ensuring a seamless workflow for note-taking and knowledge management. |
| [PDF Highlights](https://github.com/akaalias/obsidian-extract-pdf-highlights) | `obsidian-extract-pdf-highlights` | Extract highlights, underlines and annotations from your PDFs into Obsidian |
| [PDF Paste](https://github.com/Cormac-C/obsidian-paste-plugin) | `pdf-paste` | Improve copy-paste from PDFs by cleaning newlines. |
| [PDF Writer](https://github.com/jkom4/obsidian-pdf-writer) | `pdf-writer` | To write and fill a PDF. |
| [PDF++](https://github.com/RyotaUshio/obsidian-pdf-plus) | `pdf-plus` | The most Obsidian-native PDF annotation tool ever. |
| [PDF2Image](https://github.com/RasmusAChr/PDF2Images) | `pdf2img` | Turns a PDF into a series of images. |
| [Peekaboo](https://github.com/Lio5n/peekaboo) | `peekaboo` | Protect your privacy by setting a password to hide files. |
| [Peerdraft](https://github.com/peerdraft/obsidian-plugin) | `peerdraft` | Real-time, instant collaboration on Obsidian documents or folders. Whether for quick note-taking or building a team knowledge base, Peerdaft syncs with your collaborators' Obsidian vaults and also offers a Web Editor. |
| [Pending notes](https://github.com/ulisesantana/obsidian-pending-notes) | `obsidian-pending-notes` | Obsidian plugin for searching links without notes in your vault. |
| [Performium](https://github.com/ruikurenaii/performium) | `performosu` | Integrates the osu! Performance Points system to gamify your note-taking experience! |
| [Perilous Writing](https://github.com/sameersismail/obsidian-perilous-writing) | `perilous-writing` | Write continuously—or lose all progress. |
| [Periodic Notes](https://github.com/liamcain/obsidian-periodic-notes) | `periodic-notes` | Create/manage your daily, weekly, and monthly notes |
| [Periodic Table](https://github.com/R-Cramer4/Periodic-Table-Obsidian) | `periodic-table` | View a periodic table in the sidebar |
| [Permalink Opener](https://github.com/kepano/obsidian-permalink-opener) | `permalink-opener` | Opens URLs based on a permalink or slug in the file properties |
| [Perplexity Converter](https://github.com/heseber/perplexity-converter) | `perplexity-converter` | Fix references in text pasted from Perplexity. |
| [Persian Calendar](https://github.com/karfekr/obsidian-persian-calendar) | `persian-calendar` | This tool lets you see events, add and organize notes from daily to yearly on the Persian calendar, use templates with placeholders, and works with all Obsidian daily plugins. |
| [Persistent Graph](https://github.com/Sanqui/obsidian-persistent-graph) | `persistent-graph` | Adds commands to save and restore the positions of nodes on the global graph view |
| [Persistent Key-Value Store](https://github.com/iamrecursion/obsidian-pkvs) | `pkvs` | Provides a persistent key-value store for use in scripts, along with a portable web inspector. |
| [Persistent Links](https://github.com/ivan-lednev/obsidian-persistent-links) | `persistent-links` | Automatically repair internal links to blocks and headings |
| [Personal Assistant](https://github.com/edonyzpc/personal-assistant) | `personal-assistant` | AI-powered workflows to streamline the automated management of records, callouts, frontmatter, graph views, themes, and plugins in Obsidian. |
| [Personal Development Plan](https://github.com/artemkorsakov/personal-development-plan) | `personal-development-plan` | Build your Personal Development Plan. |
| [Personal OS](https://github.com/GengAd/obsidian-personal-os) | `personal-os` | Streamlining task management and productivity with a touch of gamification |
| [PF2e Statblocks](https://github.com/pixley/pf2e-statblock-for-obsidian) | `pf2e-statblocks` | Renders Pathfinder 2e statblocks cleanly, using only Markdown-based syntax. |
| [Phone to Note to Obsidian](https://github.com/dgarrett/phone-to-roam-to-obsidian) | `phone-to-roam-to-obsidian` | An unofficial Obsidian client for phonetonote.com (previously phonetoroam.com) |
| [Photopea Editor](https://github.com/KarmaToast40340/photopea-editor) | `photopea-editor` | Automatically opens images in **Photopea when clicked in your Obsidian vault. |
| [PhraseSync](https://github.com/digvijay-s-todiwal/phrasesync) | `phrasesync` | Auto-suggests internal links mid-sentence from note titles, headings, and block references. |
| [Pia viewer](https://github.com/dldisud/obsidian-pia-viewer) | `pia-viewer` | Make it look like a mobile |
| [Pickly PageBlend](https://github.com/dmitrichev/pickly-page-blend) | `pickly-page-blend` | Publish your Obsidian notes in one click |
| [Pieces for Developers](https://github.com/pieces-app/obsidian-pieces) | `pieces-for-developers` | Streamline your coding workflow in Obsidian with the Pieces For Developers plugin, offering powerful features for capturing, managing, translating, and enhancing code snippets. (Closed Source) |
| [Pin Enhancer](https://github.com/Sheeplet1/obsidian-pin-enhancer) | `pin-enhancer` | Enhances the pin function to prevent closing the pinned tab. |
| [Pinboard Sync](https://github.com/Automatt/obsidian-pinboard-sync) | `pinboard-sync` | Syncs Pinboard.in links with Daily Notes |
| [Pinned Daily Notes](https://github.com/docmarionum1/obsidian-pinned-daily-notes) | `pinned-daily-notes` | Dynamically update a pinned tab with today's daily note |
| [Pinned Notes](https://github.com/vasilcoin002/pinned-notes-plugin-obsidian) | `pinned-notes` | Pin frequently-used notes on Ribbon actions |
| [Pintora](https://github.com/amiaslee/obsidian-pintora) | `pintora` | Generates diagrams using Pintora |
| [Pinyin Replacer](https://github.com/LarrySAL/pinyin-replacer) | `pinyin_replacer` | Simple plugin to use the pinyin tones in obsidian without having to install extra keyboard layouts. |
| [Pivotal Tracker Integration](https://github.com/JonnyDeates/obsidian-pivotal-tracker-integration-plugin) | `pivotal-tracker-integration` | This is an unofficial pivotal tracker integration plugin for Obsidian. This plugin allows the user to pull stories, chores, bugs from their pivotal counterpart. |
| [Pixel Banner](https://github.com/jparkerweb/pixel-banner) | `pexels-banner` | Enhance your notes with customizable banner images, including AI-generated designs and a curated store of downloadable banners. Transform your workspace with visually stunning headers that add context, improve aesthetics, and take your note-taking beyond the ordinary. |
| [Pixel Perfect Image](https://github.com/johansan/pixel-perfect-image) | `pixel-perfect-image` | Pixel perfect 100% image resizing, copy to clipboard, show image in Finder/Explorer, edit image in external editor, and much more. |
| [Pixel Pets](https://github.com/LucasHJin/obsidian-pets) | `pixel-pets` | Adds cute and interactive pixel pets. |
| [PlantUML](https://github.com/joethei/obsidian-plantuml) | `obsidian-plantuml` | Render PlantUML Diagrams |
| [Plot Vectors and Graphs](https://github.com/nicoletanyt/obsidian-plugin-graphs) | `plot-vectors-graphs` | Generates graphs and vectors. |
| [Plotly](https://github.com/Dmytro-Shulha/obsidian-plotly) | `obsidian-plotly` | Obsidian plugin, which allow user to embed Plotly charts into markdown notes. |
| [Pluck](https://github.com/kevboh/obsidian-pluck) | `obsidian-pluck` | Quickly create notes in Obsidian from web pages. |
| [Plugin Groups](https://github.com/Mocca101/obsidian-plugin-groups) | `obsidian-plugin-groups` | Manage your Plugins through groups: Enable and disable multiple plugins through a single command, or delay the startup of plugins to speed up your Obsidian start up time. |
| [Plugin Manager](https://github.com/ohm-en/obsidian-plugin-manager) | `plugin-manager` | Extends plugin management of Obsidian.MD |
| [Plugin Reloader](https://github.com/Benature/obsidian-plugin-reloader) | `plugin-reloader` | Manually reload plugins. |
| [Plugin REPL](https://github.com/talwrii/plugin-repl) | `plugin-repl` | Provide an emacs-like read evaluate print loop to prototype plugins and do easy scripting |
| [Plugin Update Locker](https://github.com/Lemon695/obsidian-plugin-update-locker) | `plugin-update-locker` | Prevent specific plugins from being updated. |
| [Plugin Update Tracker](https://github.com/swar8080/obsidian-plugin-update-tracker) | `obsidian-plugin-update-tracker` | Know when installed plugins have updates and evaluate the risk of upgrading |
| [Plugins Annotations](https://github.com/alberti42/obsidian-plugins-annotations) | `plugins-annotations` | Allows adding personal comments to each installed plugin. |
| [Plugins Galore](https://github.com/plugins-galore/obsidian-plugins-galore) | `plugins-galore` | This is an Obsidian plugin to allow easily sideloading other plugins. |
| [Pocketbook Cloud Highlight Importer](https://github.com/lenalebt/obsidian-pocketbook-cloud-highlight-importer) | `pocketbook-cloud-highlight-importer` | Imports notes and highlights from your Pocketbook Cloud account. |
| [Podcast Note](https://github.com/marcjulianschwarz/obsidian-podcast-note) | `podcast-note` | Podcast Note lets you automatically add podcast information to your notes. |
| [PodNotes](https://github.com/chhoumann/PodNotes) | `podnotes` | Helps you write notes on podcasts. |
| [Poker](https://github.com/mAAdhaTTah/obsidian-poker) | `poker` | Easily document and view your poker hands. |
| [Poker Range](https://github.com/marplek/obsidian-poker-range) | `poker-range` | Create a poker range grid |
| [PomoBar](https://github.com/semanticdata/obsidian-pomodoro) | `pomobar` | A simple Pomodoro timer that lives in your status bar. Left click to start/stop, right click to reset when paused, middle click to cycle between work/break durations. |
| [Pomodoro Planner](https://github.com/onesvat/obsidian-pomodoro-planner) | `pomodoro-planner` | Generates a pomodoro schedule plan |
| [Pomodoro Plugin](https://github.com/tokuhirom/obsidian-pomodoro-plugin) | `obsidian-pomodoro-plugin` | This is a simple pomodoro plugin for Obsidian. |
| [Pomodoro Timer](https://github.com/eatgrass/obsidian-pomodoro-timer) | `pomodoro-timer` | A pomodoro timer that helps manage your daily focus |
| [Pomodoro Widget](https://github.com/gvvim/obsidian-pomodoro-widget) | `pomodoro-widget` | Provides a widget based on a pomodoro kitchen timer. It's designed to be haptic, and has a constant ticking sound, and an alarm sound that can be toggled. |
| [PopKit](https://github.com/zhouhua/obsidian-popkit) | `popkit` | Select text to instantly access quick tools |
| [Post To Bluesky](https://github.com/RieTamura/Post-To-Bluesky) | `post-to-bluesky` | Post selected text or entire note to Bluesky. |
| [Post Webhook](https://github.com/Masterb1234/obsidian-post-webhook) | `post-webhook` | Send notes to Webhook endpoints, for seamless integration with n8n, Make.com, and Zapier. |
| [Postfix](https://github.com/bhagyas/obsidian-postfix-plugin) | `postfix` | This plugin provides postfix completions for Obsidian. The built-in completions are provided for markdown. |
| [Potato Indexer](https://github.com/LoyalPotato/potato-indexer) | `potato-indexer` | Allow generation of a content index based on your selection or of the whole file. |
| [POWER MODE](https://github.com/zhouhua/obsidian-power-mode) | `power-mode` | Active POWER MODE!!!! |
| [Power Search](https://github.com/aviral-batra/obsidian-power-search) | `obsidian-power-search` | Searches Obsidian and Anki Notes based on current line |
| [Prettier](https://github.com/GoodbyeNJN/obsidian-plugin-prettier) | `prettier` | Format your notes with Prettier and custom formatting options. |
| [Prettier Format](https://github.com/hipstersmoothie/obsidian-plugin-prettier) | `obsidian-plugin-prettier` | Opinionated formatting for your notes. |
| [Pretty BibTeX](https://github.com/sandrofigo/obsidian-pretty-bibtex) | `obsidian-pretty-bibtex` | Shows raw BibTeX bibliography entries in a prettier way |
| [Pretty Properties](https://github.com/anareaty/pretty-properties) | `pretty-properties` | Makes note properties look more fun: adds side image, banners, list property colors and allows to hide specific properties. |
| [Previous Daily Note](https://github.com/talau/obsidian-previous-daily-note) | `previous-daily-note` | Open the previous daily note. Unlike the "Daily notes" command "Open previous daily note", it opens the previous daily note starting from today, rather than the daily note currently open. |
| [Print](https://github.com/marijnbent/obsidian-print) | `print` | Print notes and documents directly from your workspace. |
| [Prioritize](https://github.com/Tekknoman/obsidian-prio-plugin) | `prioritize` | Prioritize your tasks and notes in Obsidian. |
| [Private AI](https://github.com/gabosgab/ObsidianPrivateAI) | `private-ai` | Effortlessly chat with your notes using locally hosted AI.  Private by design, your notes never leave the device and use locally processing only. |
| [Private Mode](https://github.com/markusmo3/obsidian-private-mode) | `private-mode` | Simple #private mode |
| [ProgressBar](https://github.com/zwpaper/obsidian-progressbar) | `progressbar` | Render CodeBlock into a ProgressBar based on Time or Manually. |
| [ProgressTracker](https://github.com/vannamhh/progress-tracker) | `progress-tracker` | Track task completion with a visual progress bar in your sidebar, auto update column Kanban |
| [Project Browser](https://github.com/daledesilva/obsidian_project-browser) | `project-browser` | Replaces your new tab window with a browseable list of the files and folders in your vault. |
| [Project Euler Stats](https://github.com/artemkorsakov/project-euler-stats) | `project-euler-stats` | Get statistics from Project Euler. |
| [Project Garden](https://github.com/bgoosman/obsidian-project-garden) | `obsidian-project-garden` | See all your projects in one place |
| [Project Tasks](https://github.com/paulpaterson/obsidian-project-tasks) | `project-tasks` | Enhances task management for simple projects |
| [Proletarian Wizard Task Manager](https://github.com/cfe84/obsidian-pw) | `proletarian-wizard` | Track your tasks across all the notes in your workspace. Organize your day. Plan your work |
| [Prologue](https://github.com/joshavanier/prologue) | `prologue` | Display a random quote or reminder on the new tab page. |
| [Prominent Bookmarked Files](https://github.com/javalent/prominent-files) | `obsidian-prominent-starred-files` | Prominently display bookmarked notes in the file explorer |
| [Prompt](https://github.com/hungsu/obsidian-prompt) | `prompt` | Shows a random text prompt when triggered |
| [Prompt ChatGPT](https://github.com/Coduhuey/ChatGPT-Prompt-Plugin-For-Obsidian) | `chatgpt-prompt` | Send templated prompts to chatgpt when you open a file |
| [PromptCrafter](https://github.com/fabricehong/obsidian-prompt-crafter-plugin) | `prompt-crafter` | Create reusable, modular prompts. |
| [Proofreader](https://github.com/chrisgrieser/obsidian-proofreader) | `proofreader` | AI-based proofreading and stylistic improvements for your writing. Changes are inserted as suggestions directly in the editor, similar to suggested changes in word processing apps. |
| [Protected Note](https://github.com/mmiksaa/obsidian-protected-note) | `protected-note` | Set Password and Protect your notes from other people. Encrypt and Decrypt all notes! |
| [ProZen](https://github.com/cmoskvitin/obsidian-prozen) | `obsidian-prozen` | Enter Zen mode to focus on writing. The plugin expands current tab to full screen removing everything but content. |
| [Pseudo Mica](https://github.com/aaaaalexis/obsidian-pseudo-mica) | `pseudo-mica` | Customize translucent window effects on Windows and macOS. |
| [Pseudocode](https://github.com/ytliu74/obsidian-pseudocode) | `pseudocode-in-obs` | This is an obsidian plugin that helps to render a LaTeX-style pseudocode inside a code block. |
| [Publish and GitHub URL](https://github.com/kometenstaub/copy-publish-url) | `copy-publish-url` | Copy or open the URL of the corresponding note on your Publish site. You can also open its Git commit history on GitHub. |
| [Publish Note to Mowen Note](https://github.com/zhuSilence/obsidian-mowen-plugin) | `publish-note-to-mowen` | Publish note to Mowen note mini program. |
| [Publish to DEV](https://github.com/stroiman/obsidian-dev-publish) | `publish-to-dev` | Publish and update notes as articles on DEV (https://dev.to) |
| [Publish to Discourse](https://github.com/woodchen-ink/obsidian-publish-to-discourse) | `publish-to-discourse` | Publish notes to the Discourse forum. |
| [Publish url](https://github.com/HananoshikaYomaru/obsidian-publish-url) | `publish-url` | Obsidian Publish url to the clipboard |
| [Publish with Flowershow](https://github.com/flowershow/obsidian-flowershow) | `flowershow` | Publish your vault as a website with Flowershow. |
| [PubScale](https://github.com/piriwata/pubScale) | `pubscale` | Seamlessly sync markdown notes into PlanetScale tables. |
| [Pug Templates](https://github.com/nicholas-wilcox/pug-templates-obsidian-plugin) | `pug-templates` | Use the Pug templating engine in your vault. |
| [Pure Chat LLM](https://github.com/TheJusticeMan/pure-chat-llm) | `pure-chat-llm` | Turn notes into conversations with chatGPT |
| [pycalc](https://github.com/pycalc-plugin/obsidian) | `pycalc` | Executing Python code directly within the editor by pressing the Enter key. |
| [QB Reader Parser](https://github.com/J-Barta/qb-reader-parser) | `qb-reader-parser` | Parse tossups from QB Reader into individual clues to send to Anki. |
| [Qiniu Image Uploader](https://github.com/jianzs/obsidian-qiniu-image-uploader) | `qiniu-image-uploader` | Uploads images from your clipboard to qiniu.com and embeds uploaded image to your note. |
| [qmd as md](https://github.com/danieltomasz/qmd-as-md-obsidian) | `qmd-as-md-obsidian` | This plugin provides an initial support for viewing files with .qmd extension. QMD files contain a combination of markdown and executable code cells and are a format supported by Quarto open source publishing system. |
| [QR Code Generator](https://github.com/rudimuc/obsidian-qrcode) | `obsidian-qrcode-plugin` | This is a QR Code Generator plugin for Obsidian. |
| [Quadro](https://github.com/chrisgrieser/obsidian-quadro) | `quadro` | Qualitative Data Analysis (QDA) for social scientists. An open alternative to `MAXQDA` and `atlas.ti`, using Markdown to store data and research codes. |
| [Quaily](https://github.com/lyricat/obsidian-quail) | `quail` | Save, publish, delivery notes via Quaily.com as newsletters and blogs. |
| [Quarto Exporter](https://github.com/AndreasThinks/obsidian-to-quarto-exporter) | `quarto-exporter` | Export notes to Quarto-compatible QMD files. |
| [Quartz Syncer](https://github.com/saberzero1/quartz-syncer) | `quartz-syncer` | Manage and publish your notes to Quartz, the fast, batteries-included static-site generator. |
| [Query all the things](https://github.com/sytone/obsidian-queryallthethings) | `qatt` | Execute SQL base queries against your data in Obsidian and render it how you want using templates. |
| [Query JSON](https://github.com/Rooyca/query-json) | `query-json` | Read, query and work with JSON. |
| [QueryDash](https://github.com/liufree/obsidian-querydash) | `querydash` | The new view for bases refers to an updated or additional interface that allows users to interact with base data in a different way, such as through enhanced search, sorting, and pagination features, similar to Notion. This improves usability and data management within your application. It was originally a new view for dataview, but now its functionality has been extended to bases. |
| [Quick Cards](https://github.com/abcamus/obsidian-quick-card) | `quick-cards` | cardify your files |
| [Quick Emoji](https://github.com/asibilia/obsidian-quick-emoji) | `quick-emoji` | Quick, in-editor, emoji inserting. Type ":" to start selecting an emoji to insert. |
| [Quick Explorer](https://github.com/pjeby/quick-explorer) | `quick-explorer` | Perform file explorer operations (and see your current file path) from the title bar, using the mouse or keyboard |
| [Quick File Name](https://github.com/Wapply/obsidian-quick-file-name) | `quick-file-name` | Generates a note with a random string as its name. |
| [Quick Latex](https://github.com/joeyuping/quick_latex_obsidian) | `quick-latex` | Speedup latex math typing with auto fraction, custom shorthand, align block shortcut, matrix shortcut...etc |
| [Quick Links](https://github.com/iafisher/obsidian-quick-links) | `quick-links` | Create quick link shortcuts to Wikipedia and other sites |
| [Quick Matrix](https://github.com/thewheelbarrow/quick-matrix) | `quick-matrix` | Adds command to make LaTeX matrices quickly. |
| [Quick Nav](https://github.com/exoticknight/quick-nav) | `quick-nav` | Enhance your editing experience by unleashing the hidden power of shortcuts |
| [Quick note](https://github.com/jamesgreenblue/obsidian-quicknote) | `quicknote` | Create a quick note in a floating window (on command or by right-clicking the Obsidian app icon) |
| [Quick Notes](https://github.com/SeanMcOwen/Quick-Note-Obsidian-Plugin) | `quick-notes` | Speeds up some note taking abilities and allows for creating notes/links in the background |
| [Quick Peek Sidebar](https://github.com/bwya77/obsidian-quick-peek-sidebar) | `quick-peek-sidebar` | Opens the left and/or right side panel by hovering over it. |
| [Quick Preview](https://github.com/RyotaUshio/obsidian-quick-preview) | `quick-preview` | Quickly preview a suggestion before selecting it in link suggestions & quick switcher. |
| [Quick Select](https://github.com/itsonlyjames/obsidian-quick-select) | `quick-open` | Quickly select items in any modal using keyboard shortcuts. Supercharge your workflow with fast, efficient item selection in Obsidian modals. |
| [Quick Share Note to gist](https://github.com/chaintng/quick-share-note-to-gist) | `quick-share-note-to-gist` | Quick share notes to GitHub gist and its image by upload images to Imgur. |
| [Quick snippets and navigation](https://github.com/ieviev/obsidian-keyboard-shortcuts) | `quick-snippets-and-navigation` | Keyboard navigation up/down for headings - Quick switcher extensions - Copy code block via keyboard shortcut - Configurable code block and callout snippets |
| [Quick Switcher++](https://github.com/darlal/obsidian-switcher-plus) | `darlal-switcher-plus` | Enhanced Quick Switcher, search open panels, and symbols. |
| [Quick Tagger](https://github.com/Gorkycreator/obsidian-quick-tagger) | `quick-tagger` | Add and remove tags quickly. Tag search results, bulk tag, and add dedicated buttons/commands for your favorites! |
| [QuickAdd](https://github.com/chhoumann/quickadd) | `quickadd` | Quickly add new pages or content to your vault. |
| [QuickLink](https://github.com/Jamailar/QuickLink-Obsidian) | `quicklink` | Quickly create links to files using @ trigger character |
| [Quickly](https://github.com/tmfelwu/obsidian-inbox) | `quickly` | Quickly empowers you to add your thoughts into obsidian with a shortcut key. |
| [QuickShare](https://github.com/mcndt/obsidian-quickshare) | `obsidian-quickshare` | Securely share your Obsidian notes with one click. Notes are end-to-end encrypted. No API keys or configuration required. |
| [Quiet Outline](https://github.com/guopenghui/obsidian-quiet-outline) | `obsidian-quiet-outline` | Make outline quiet and more powerful, including no-auto-expand, rendering heading as markdown, and search support. |
| [Quip](https://github.com/sblakey/obsidian-quip) | `quip` | This plugin provides commands to publish Markdown documents to Quip.com |
| [Quiz Generator](https://github.com/ECuiDev/obsidian-quiz-generator) | `quiz-generator` | Generate interactive flashcards from your notes using models from OpenAI (ChatGPT), Google (Gemini), Ollama (local LLMs), and more. Or manually create your own to use with the quiz UI. |
| [Quote of the Day](https://github.com/twentytwokhz/quote-of-the-day) | `quote-of-the-day` | Inserts random quotes in the editor |
| [Quote Share](https://github.com/nguyenvanduocit/quote-share) | `quote-share` | With this plugin, you can easily generate beautiful gradient images from text and share them on social media. |
| [Quoth](https://github.com/erykwalder/quoth) | `quoth` | More flexible embedding. Embed precise selections, inline embeds, optionally include author and title. |
| [Quran](https://github.com/AmmarCodes/obsidian-quran-helper-plugin) | `quran-helper` | Find and insert any Quran Ayah (verse) in your notes. |
| [Quran Lookup](https://github.com/abuibrahim2/quranlookup) | `obsidian-quran-lookup` | This is a Quran Lookup plugin for Obsidian. This replaces chapter:verse shorthand with verse text in arabic and translation. |
| [R.E.L.A.X.](https://github.com/Syr0/R.E.L.A.X.) | `relax` | Multi-regex management for data linking and batch processing across selection, files and folders. Ideal for academics, data scientists, forensics, reverse-engineerer and knowledge workers. Enables dynamic data organization and can be used to standardize links or as text-search. Streamline note-taking, data analysis, and report generation with intuitive regex pattern application and modification. |
| [Radial timeline](https://github.com/EricRhysTaylor/Radial-Timeline) | `radial-timeline` | A radial timeline for long-form creative fiction writing that displays scenes organized by act, subplot, and numeric order for a complete view of the project. |
| [Rainbow Folders Fixer](https://github.com/dee158/obsidian-rainbow-folders-fixer) | `rainbow-folders-fixer` | Stop rainbow folders from changing colors when you scroll through the File explorer. |
| [Rainbow-Colored Sidebar](https://github.com/Kovah/obsidian-rainbow-colored-sidebar) | `rainbow-colored-sidebar` | Automatically color your sidebar like a rainbow. No configuration needed. 9 themes included. |
| [Raindrop Highlights](https://github.com/kaiiiz/obsidian-raindrop-highlights-plugin) | `obsidian-raindrop-highlights` | Sync your Raindrop.io highlights. |
| [Random broken link](https://github.com/janTatesa/obsidian-open-random-broken-link) | `random-broken-link` | Expand your knowledge by visiting random broken links. |
| [Random names](https://github.com/palfrey/obsidian-random-names) | `random-names` | Generates random names |
| [Random Number Generator](https://github.com/iRewiewer/obsidian-random-numbers-generator-plugin) | `random-numbers-generator` | Insert a random number. |
| [Random Structural Diary](https://github.com/ShockThunder/RandomStructuralDiary) | `random-structural-diary-plugin` | This is a plugin for picking random questions from prepared question list. It allows you answer on different questions each time. |
| [Random To-Do](https://github.com/NatiAris/obsidian-random-todo) | `obsidian-random-todo` | Open a random file containing your custom to-do marker, or a random marker at its position |
| [Random Wikipedia Article](https://github.com/SpencerF718/obsidian-random-wikipedia) | `random-wikipedia-article` | Generates a note for a random Wikipedia article. |
| [random-retrieval](https://github.com/JeanJean-rxl/random-retrieval-plugin) | `random-retrieval` | Random Note Retrieval based on LLMs. |
| [Rant-Lang](https://github.com/lanice/obsidian-rant) | `obsidian-rant` | Thin wrapper around the Rant language Rust crate |
| [Rapid AI](https://github.com/ahmed3developer/rapid-ai) | `rapid-ai` | AI Assistant for selected text and generating content with Markdown. Shortcuts and quick action buttons provide instant AI assistance. It provides a high availability API for unlimited Chat GPT request rates, so you can ensure smooth work for any workload. |
| [Rapid Notes](https://github.com/valteriomon/obsidian-rapid-notes) | `obsidian-rapid-notes` | Create and place notes quickly in specific folders based on predefined prefixes. |
| [React Components](https://github.com/elias-sundqvist/obsidian-react-components) | `obsidian-react-components` | This is a plugin for Obsidian. It allows you to write and use React components with Jsx inside your Obsidian notes. |
| [Reactive Notes](https://github.com/Prodigist/ReactiveNotes) | `reactive-notes` | Transform your vault into a reactive computational environment. Create dynamic React components directly in your notes. |
| [Read Later](https://github.com/Canna71/obsidian-readlater) | `obsidian-readlater` | Synch web pages to markdown and integrate with read-it-later apps (Pocket, Instapaper) |
| [Readability Score](https://github.com/zuchka/obsidian-readability) | `readability-score` | Score the readabilty of your writing using the Flesch Reading Ease (FRE) formula. |
| [Readavocado Sync](https://github.com/innneang/obsidian-readavocado-sync) | `readavocado-sync` | Sync your Readavocado highlights with Obsidian |
| [Readeck Importer](https://github.com/makebit/obsidian-readeck-importer) | `readeck-importer` | Import bookmarks from Readeck. |
| [Reader Mode](https://github.com/dominikmayer/obsidian-reader-mode) | `reader-mode` | Ensures notes are always opened in reader mode. |
| [Reading comments](https://github.com/BumbrT/obsidian-reading-comments) | `reading-comments` | Plugin allows you to create comments while you read books or articles in Obsidian. Comments could be grouped hierarchically by tags. |
| [Reading progress desktop](https://github.com/qian-shen/obsidian-reading-progress-desktop) | `reading-progress-desktop` | A progress bar for some views in the status bar(desktopAPP). |
| [Reading Time](https://github.com/avr/obsidian-reading-time) | `obsidian-reading-time` | Add the current note's reading time to Obsidian's status bar. |
| [Reading View Enhancer](https://github.com/Galacsh/obsidian-reading-view-enhancer) | `reading-view-enhancer` | Enhances reading view. Use arrow keys to navigate between blocks or toggle collapse. |
| [Reading View j/k Scroll](https://github.com/LukasKorotaj/Scroll-With-j-k-in-Obsidian) | `scroll-with-jk` | Scroll in reading view with j/k keys. Scroll to top with gg and to bottom with G. |
| [ReadItLater](https://github.com/DominikPieper/obsidian-ReadItLater) | `obsidian-read-it-later` | Save online content to your Vault, utilize embedded template engine and organize your reading list to your needs. Preserve the web with ReadItLater. |
| [Readwise Community](https://github.com/renehernandez/obsidian-readwise) | `obsidian-readwise` | Sync Readwise highlights into your notes |
| [Readwise mirror](https://github.com/jsonMartin/readwise-mirror) | `readwise-mirror` | Mirror your Readwise library directly to an Obsidian vault |
| [Readwise Official](https://github.com/readwiseio/obsidian-readwise) | `readwise-official` | Official Readwise <-> Obsidian integration |
| [Recall](https://github.com/martin-jw/obsidian-recall) | `obsidian-recall` | A flexible and configurable Spaced Repetition System built into Obsidian. |
| [Recent Files](https://github.com/tgrosinger/recent-files-obsidian) | `recent-files-obsidian` | List files by most recently opened |
| [Recent Notes](https://github.com/kamil-rudnicki/obsidian-recent-notes) | `recent-notes` | List of recently edited notes with previews by time periods |
| [Recent Tab Switcher](https://github.com/samuelrawrs/recent-tab-switcher) | `recent-tab-switcher` | Switch to the most recently used tab. |
| [Recently Added Files](https://github.com/Lemon695/obsidian-recently-added-files) | `recently-added-files` | List files by last added, including pictures, MP4s, PDFs etc. |
| [Recipe Grabber](https://github.com/seethroughdev/obsidian-recipe-grabber) | `recipe-grabber` | Quickly grab the important contents of any online recipe. |
| [Recipe view](https://github.com/lachsh/obsidian-recipe-view) | `recipe-view` | View your notes as interactive recipe cards while you cook. |
| [ReClipped Official](https://github.com/tech-reclipped/ReClipped-Obsidian-Official) | `reclipped-official` | Official ReClipped and Obsidian integration |
| [Recursive Copy](https://github.com/StructByLightning/obsidian-recursive-copy) | `recursive-copy` | Recursively copies all markdown files in a folder, concatenates them, and copies them into the clipboard. Useful for quickly loading context into AI. Can be triggered by right clicking a folder and selecting the context menu item, or by binding a key (will copy everything in the active file's folder). |
| [Red Pen](https://github.com/lucasmelin/red-pen) | `red-pen` | Red Pen acts as a proofreader for your writing. |
| [Redirect](https://github.com/jglev/obsidian-redirect) | `obsidian-redirect` | An Obsidian (https://obsidian.md) plugin for redirecting links based on YAML frontmatter. |
| [Reference Map](https://github.com/anoopkcn/obsidian-reference-map) | `reference-map` | Reference and citation map for literature review and discovery |
| [Reflection](https://github.com/brandonkboswell/reflection) | `reflection` | Shows daily and weekly notes from this day in years past. |
| [Refresh Any View](https://github.com/mnaoumov/obsidian-refresh-any-view) | `refresh-preview` | Allows to refresh any view without reopening it. |
| [Regex Find/Replace](https://github.com/Gru80/obsidian-regex-replace) | `obsidian-regex-replace` | Find and replace text using regular expressions. |
| [Regex Line Filter](https://github.com/64MM4-KN1F3/regex-line-filter) | `regex-line-filter` | Filters the active note to show only lines matching a regex, allowing edits. |
| [Regex Mark](https://github.com/Mara-Li/obsidian-regex-mark) | `regex-mark` | Add custom CSS classes to text based on regular expressions. |
| [Regex Pipeline](https://github.com/No3371/obsidian-regex-pipeline) | `obsidian-regex-pipeline` | Allows users setup custom regex rules to automatically format notes. |
| [Related Notes](https://github.com/mrboxtobox/obsidian-related-notes) | `related-notes` | Discover related notes and uncover missed connections. |
| [Related Notes by Tag](https://github.com/chrishoward-projects/related-notes-by-tag) | `related-notes-by-tag` | Displays list of notes in the sidebar that share tags with the currently active note. |
| [Related Notes Finder](https://github.com/lifegems/obsidian-related-notes-finder) | `obsidian-related-notes-finder` | An Obsidian plugin that adds extra features for finding related notes. |
| [Relation Pane](https://github.com/mottox2/obsidian-relation-pane) | `obsidian-relation-pane` | This plugin displays a panel that summarize relations between notes. |
| [Relative Find](https://github.com/phibr0/obsidian-relative-find) | `obsidian-relative-find` | This Plugin lets you search relative to your Cursor Position. |
| [Relative Line Numbers](https://github.com/nadavspi/obsidian-relative-line-numbers) | `obsidian-relative-line-numbers` | Enables relative line numbers in editor mode |
| [Relative Timestamps](https://github.com/agctute/relative-timestamps) | `relative-timestamps` | Track the time between log entries |
| [Relativenumber (relative line numbers)](https://github.com/thisdotrob/obsidian-relativenumber-plugin) | `obsidian-relativenumber` | Displays relative line numbers in the editor's gutter. |
| [Relay](https://github.com/No-Instructions/Relay) | `system3-relay` | Collaborate in real time with live cursors. Create multiplayer folders and manage user access. |
| [Release Timeline](https://github.com/cakechaser/obsidian-release-timeline) | `obsidian-release-timeline` | Release timeline rendered based on notes metadata with a dataview-like syntax. |
| [Remaining reading time](https://github.com/ununnamed/remaining-reading-time) | `remaining-reading-time` | Shows the remaining reading time for the current note depending on the cursor position. |
| [Remember cursor position](https://github.com/dy-sh/obsidian-remember-cursor-position) | `remember-cursor-position` | Remember cursor and scroll position for each note |
| [Remember File State](https://github.com/ludovicchabant/obsidian-remember-file-state) | `obsidian-remember-file-state` | Remembers cursor position, selection, scrolling, and more for each file |
| [Remember Scrollposition](https://github.com/s-blu/obsidian-remember-scrollposition) | `remember-scrollposition` | Remembers the scroll position in your notes and returns you to your last position upon opening a note. |
| [Reminder](https://github.com/uphy/obsidian-reminder) | `obsidian-reminder-plugin` | Reminder plugin for Obsidian. This plugin adds feature to manage TODOs with reminder. |
| [Remote Fetch](https://github.com/Shaharyar-developer/remote-fetch) | `remote-fetch` | Download files from URLs directly into your vault with CORS proxy support. |
| [Remotely Save](https://github.com/remotely-save/remotely-save) | `remotely-save` | Yet another unofficial plugin allowing users to synchronize notes between local device and the cloud service. |
| [Remotely Sync](https://github.com/sboesen/remotely-sync) | `remotely-secure` | Security and feature updates for the remotely-save unofficial plugin allowing users to synchronize notes between local device and the cloud service. Not backwards compatible. |
| [Remove Empty Folders](https://github.com/fnya/remove-empty-folders) | `remove-empty-folders` | Easily remove empty folders. |
| [Remove HTML Tag](https://github.com/gitcpy/obsidian-remove-html-tag) | `remove-html-tag` | Remove HTML tags from Markdown files |
| [Remove Newlines](https://github.com/HandcartCactus/obsidian-remove-newlines) | `remove-newlines` | Remove newlines or blank lines from selected or pasted text. |
| [Remove Unused Block IDs](https://github.com/isdmg/obsidian-remove-unused-block-ids) | `remove-unused-block-ids` | Remove unused block ids in your vault. |
| [Rename File to Selection](https://github.com/AavaGames/obsidian-rename-file-to-selection) | `rename-file-to-selection` | Rename your file to the current text selection. |
| [Rendered Block Link Suggestions](https://github.com/RyotaUshio/obsidian-rendered-block-link-suggestions) | `rendered-block-link-suggestions` | Upgrade Obsidian's built-in link suggestions with block markdown rendering. |
| [Repeat](https://github.com/prncc/obsidian-repeat-plugin) | `repeat-plugin` | Review notes using periodic or spaced repetition. |
| [Replace All](https://github.com/patrickchiang/obsidian-replace-all) | `replace-all` | Replace all in vault. |
| [Replace Pencil](https://github.com/penyt/replace-pencil) | `replace-pencil` | Easily replace the custom variable in the code block. |
| [Replicate](https://github.com/dsebastien/obsidian-replicate) | `replicate` | Replicate.com integration. Use AI models with ease |
| [RescueTime](https://github.com/Tatz884/RescueTime-Obsidian) | `rescuetime` | View your RescueTime data in Obsidian. |
| [Research Quest](https://github.com/narthur/research-quest) | `research-quest` | Use AI to generate and track research questions based on your notes. |
| [Reset Font Size](https://github.com/luckman212/obsidian-reset-font-size) | `obsidian-reset-font-size` | Adds button and command to reset the font size back to its default value. |
| [Restore Tab Key](https://github.com/jrymk/restore-tab-key) | `restore-tab-key` | Restore tab key behaviour: tab key inserts a tab character, the way it should be. |
| [Reveal Active File Button](https://github.com/claremacrae/reveal-active-file-button-plugin) | `reveal-active-file-button` | Add a button to the top of the File Explorer, to reveal the active file. |
| [Reveal Folded](https://github.com/d7sd6u/obsidian-reveal-folded) | `reveal-folded` | Reveal the current file in the file explorer while collapsing all other tree items. |
| [Reverse Prompter](https://github.com/ryanhalliday/obsidian-reverse-prompter) | `reverse-prompter` | Generate prompts to keep you writing with AI. |
| [Review](https://github.com/ryanjamurphy/review-obsidian) | `review-obsidian` | Add a link to the current note to a daily note on a future date (or a past date, you time traveller). |
| [Review Notes Plugin](https://github.com/tjandy98/obsidian-review-notes-plugin) | `obsidian-review-notes-plugin` | This plugin shows recently modified and newly created files |
| [Rewarder](https://github.com/Gnopps/obsidian-rewarder) | `obsidian-rewarder` | Gives you rewards for completing tasks/todos, highly configurable. |
| [Ribbon Divider](https://github.com/andrewmcgivery/obsidian-ribbon-divider) | `ribbon-divider` | Allows you to add dividers to the ribbon to space out your icons. |
| [Rich Foot](https://github.com/jparkerweb/rich-foot) | `rich-foot` | Adds backlink tags and created/modified dates to the footer of your notes. |
| [Rich Links](https://github.com/dhamaniasad/obsidian-rich-links) | `obsidian-rich-links` | Rich Links plugin for Obsidian. |
| [Rich Text Editor Shortcuts](https://github.com/joshuawootonn/obsidian-rich-text-editor-shortcuts) | `rich-text-editor-shortcuts` | Create and toggle checkboxes, paste links wrapping your current selection, and toggle underline without leaving the keyboard. |
| [Ridian](https://github.com/MichelNivard/Ridian) | `ridian` | Execute R code blocks and display outputs and plots & render documents with Quarto within Obsidian. |
| [Ring a secretary](https://github.com/vrtmrz/ring-a-secretary) | `ring-a-secretary` | Yet another ChatGPT-powered digital secretary |
| [Rofi Helper](https://github.com/digitalsignalperson/obsidian-rofi-helper) | `rofi-helper` | This plugin adds a leaf id parameter to the URI protocol for switching between open obsidian tabs with Rofi. A sample Rofi script is included. |
| [Role Switch](https://github.com/zafrem/obsidian-role-switch) | `role-switch` | Switch between different work roles (developer, writer, researcher, etc.) with intentional transitions and session tracking. |
| [Rollover Daily Todos](https://github.com/lumoe/obsidian-rollover-daily-todos) | `obsidian-rollover-daily-todos` | This Obsidian.md plugin rolls over incomplete TODOs from the previous daily note to today's daily note. (https://obsidian.md). (Originally created by Matthew Sessions) |
| [Rollover Weekly Todo](https://github.com/shsethi/obsidian-rollover-weekly-todos) | `rollover-weekly-todo` | Rollover todo items from the previous weekly note. |
| [Root Folder Context Menu](https://github.com/mnaoumov/obsidian-root-folder-context-menu) | `root-folder-context-menu` | Enables context menu for vault root folder |
| [RPG Manager](https://github.com/carlonicora/obsidian-rpg-manager) | `rpg-manager` | Manage your Tabletop Role Playing Game Campaigns in Obsidian |
| [RPG Stat Tracker](https://github.com/name/obsidian-rpg) | `rpg-stat-tracker` | RPG-like stat tracker. |
| [Rss Copyist](https://github.com/aoout/obsidian-rss-copyist) | `rss-copyist` | Get the rss articles as mdfiles. |
| [RSS Dashboard](https://github.com/amatya-aditya/obsidian-rss-dashboard) | `rss-dashboard` | A dashboard for organizing and consuming RSS feeds, YouTube channels, and podcasts with smart tagging, media playback, and seamless content flow. |
| [Rsync](https://github.com/GanapathyRaman/rsync-plugin) | `rsync` | Sync files across devices using rsync tool. |
| [RTL Math Text](https://github.com/orelby/obsidian-rtl-math-text-plugin) | `rtl-math-text` | Mix right-to-left and left-to-right text in math expressions using configurable commands. |
| [RTL Support](https://github.com/esm7/obsidian-rtl) | `obsidian-rtl` | Extended Right to Left (RTL) support for languages like Arabic, Hebrew and Persian (Farsi). |
| [ruby.wasm](https://github.com/geeknees/obsidian-ruby-wasm-plugin) | `ruby-wasm` | Run ruby code in your notes using WebAssembly |
| [Ruled template](https://github.com/YPetremann/obsidian-ruled-template) | `ruled-template` | Select templates automaticaly based on rules at file creation. |
| [Run](https://github.com/HananoshikaYomaru/obsidian-run) | `run` | Generate markdown from dataview query and javascript |
| [RunJS](https://github.com/eoureo/obsidian-runjs) | `runjs` | Run easily JavaScript codes for managing Obsidian and its notes. |
| [Runsh](https://github.com/Deedone/obsidian-runsh) | `runsh` | Create buttons that run shell commands from your notes. |
| [S3 attachments storage](https://github.com/ttax00/obsidian-s3) | `s3-attachments-storage` | An Obsidian plugin for storage and retrieval of media attachments on S3 compatible services. |
| [S3 Image Uploader](https://github.com/jvsteiner/s3-image-uploader) | `s3-image-uploader` | This is an image uploader for Obsidian that allows you to self host images on AWS s3. This plugin is supported by advertisements. |
| [S3agle](https://github.com/turnercore/s3agle) | `s3agle` | Use S3 providers and/or Eagle to manage vault attachments locally and remotely. |
| [Safe Filename Linter](https://github.com/sneakyfoxes/obsidian-safe-filename-linter) | `safe-filename-linter` | Lints filenames for invalid or troublesome characters |
| [SafeLearn Formatter](https://github.com/UnterrainerInformatik/safeLearn-Obsidian-plugin) | `safelearn-formatter` | Offers visual aids for tags specific for SafeLearn (an open-source project) such as ##fragment, permission blocks, and side-by-side layouts for Reveal.js. |
| [Sakana Widget](https://github.com/Quorafind/obsidian-sakana-widget) | `obsidian-sakana-widget` | Add the Sakana! Widget to your own Obsidian! |
| [SamePage](https://github.com/samepage-network/obsidian-samepage) | `samepage` | Official Obsidian client into the inter-TFT-protocol |
| [Sankey](https://github.com/finnromaneessen/obsidian-sankey) | `sankey` | Create Sankey diagrams in your notes. |
| [Save as Gist](https://github.com/ghedamat/obsidian-save-as-gist) | `obsidian-save-as-gist` | Saving your current note as Gist on github |
| [Scales and Chords](https://github.com/egradman/scales-chords) | `scales-chords` | Use this plugin to capture musical tab notation in your Obsidian vault.  Chords will become clickable links to modal images (provided by scales-chords.com) |
| [Scholar](https://github.com/lolipopshock/obsidian-scholar) | `scholar` | Streamline Research Workflow in Obsidian |
| [Scrambling Title Animations](https://github.com/DvorakDwarf/scrambling-title-animations) | `scrambling-title-animations` | Animates the title of any note you open by scrambling and revealing it in several visually appealing ways. |
| [Scratchpad](https://github.com/kvh03/obsidian-scratchpad) | `scratchpad` | Take temporary notes and draw freehand in a sidebar scratchpad. |
| [screen.garden](https://github.com/screendotgarden/screengarden-obsidian) | `screengarden-obsidian` | Collaborate, share, and edit on the web with screen.garden. |
| [Screwdriver](https://github.com/vrtmrz/obsidian-screwdriver) | `obsidian-screwdriver` | Utility to put any files in and out under your vault. |
| [Scribe](https://github.com/Mikodin/obsidian-scribe) | `scribe` | Record, transcribe, and transform voice notes into structured insights. Leverage Whisper or AssemblyAI and ChatGPT to fill in gaps, generate summaries, and visualize ideas — all seamlessly integrated within Obsidian. |
| [Script Launcher](https://github.com/AlessandroRuggiero/script-launcher) | `script-launcher` | This pulgin allows you to launch scripts from the Obsidian app. You can add scripts shortcuts on your bottom bar and launch them with just one click! |
| [Scripture Indexer](https://github.com/jdrbrn/obsidian-scripture-indexer) | `scripture-indexer` | Indexes references to scriptures in notes. |
| [Scroll Offset](https://github.com/lijyze/scroll-offset) | `obsidian-scroll-offset` | Preserve minmium distances before and after cursor. |
| [Scroll Speed](https://github.com/flolu/obsidian-scroll-speed) | `scroll-speed` | This plugin allows you to change the scroll speed inside Obsidian notes. |
| [Scroll to Top](https://github.com/cloudhao1999/obsidian-scroll-to-top-plugin) | `obsidian-scroll-to-top-plugin` | This is a plugin for Obsidian that adds a button to scroll to the top of the current note. |
| [Scroller](https://github.com/coignard/obsidian-scroller) | `scroller` | Adds typewriter mode, focus mode and commands to quickly scroll to the top or bottom of note. |
| [Scrolling](https://github.com/omeyenburg/obsidian-scrolling) | `scrolling` | Keep the cursor centered, disable code wrapping, remember scroll position, enable image zooming and more. |
| [Scrolls To Nav Top](https://github.com/mariomui/scroll-to-nav-top) | `scroll-to-nav-top` | Scrolls File Explorer To Top Position. |
| [Scrybble](https://github.com/Scrybbling-together/scrybble) | `scrybble.ink` | Synchronize highlights from your ReMarkable to Obsidian! |
| [Seafile](https://github.com/conql/obsidian-seafile) | `seafile` | Sync notes across devices using Seafile. |
| [Search Everywhere](https://github.com/Mom0aut/obsidian-search-everywhere) | `obsidian-search-everywhere-plugin` | Search Everywhere with pressing Double Shift like in IntelliJ |
| [Search In Canvas](https://github.com/Quorafind/Obsidian-Search-In-Canvas) | `search-in-canvas` | Search text in canvas |
| [Search on Internet](https://github.com/HEmile/obsidian-search-on-internet) | `search-on-internet` | Add context menu items to search the internet within Obsidian. |
| [Search Templates Library](https://github.com/Pentchaff/obsidian-search-library) | `template-search-library` | Allows you to save search templates for future re-use |
| [Search++](https://github.com/nhaouari/searchpp) | `searchpp` | Allow inserting text context search results on the active note, the plugin is based on the plugin mrj-text-expand-witb-text of MrJackphil. |
| [Second Window](https://github.com/javalent/second-window) | `image-window` | Allow images & notes to be viewed in new Obsidian windows. |
| [Select & Complete](https://github.com/macro21KGB/select-and-complete) | `select-and-complete` | Select something and let the AI complete it for you. |
| [Select current line](https://github.com/gokulk16/select-current-line-plugin) | `select-current-line` | Selects the current line where the cursor is placed. Press 'ESC' button to select. |
| [Select word](https://github.com/ConnorEspino/ObsidianSelectWord) | `select-word` | Selects the word that is closest to the caret. |
| [Self-hosted LiveSync](https://github.com/vrtmrz/obsidian-livesync) | `obsidian-livesync` | Community implementation of self-hosted livesync. Reflect your vault changes to some other devices immediately. Please make sure to disable other synchronize solutions to avoid content corruption or duplication. |
| [Semantic Canvas](https://github.com/aarongilly/obsidian-semantic-canvas-plugin) | `semantic-canvas` | Create semantic knowledge graphs using Canvases to modify note properties graphically. |
| [Semantic Search](https://github.com/bbawj/obsidian-semantic-search) | `bbawj-semantic-search` | Semantic search for files using text embeddings |
| [Send Note](https://github.com/jvsteiner/send-note) | `send-note` | Instantly send a note, to other obsidian users so they can import them into their vault. It uses AWS S3 as a storage backend. Data is shared encrypted by default, and only you and the person you send it to have the key. |
| [Send Tasks to OmniFocus](https://github.com/lizard-heart/obsidian-to-omnifocus) | `tasks-to-omnifocus` | An Obsidian plugin will extract tasks from the current note and create them in OmniFocus. |
| [Send to Canvas](https://github.com/wenlzhang/obsidian-send-to-canvas) | `send-to-canvas` | Send tasks, blocks, and notes to Canvas files as plain text, links, and embeds. |
| [Send to Ghost](https://github.com/Southpaw1496/obsidian-send-to-ghost) | `send-to-ghost` | Send and publish notes to your Ghost blog with a single click |
| [Sentence Navigator](https://github.com/timhor/obsidian-sentence-navigator) | `obsidian-sentence-navigator` | Manipulate sentences as a unit of movement. Select, move and delete by whole sentences. |
| [Sentence Rhythm](https://github.com/adamfletcher/obsidian-sentence-rhythm) | `sentence-rhythm` | Adds toggleable colored highlights to sentences based on their length so you can easily see the rhythm of your writing. |
| [Sentinel](https://github.com/gsarig/obsidian-sentinel) | `sentinel` | Trigger actions based on document visibility changes. |
| [Sequence Hotkeys](https://github.com/moolmanruan/obsidian-sequence-hotkeys) | `obsidian-sequence-hotkeys` | This plugin allows you to set hotkeys with key sequences instead of a single chord. |
| [Serendipity](https://github.com/ggauravr/obsidian-serendipity-plugin) | `serendipity` | Forces serendipitous discoveries by displaying random notes from your vault each time you open the app |
| [Session Notes](https://github.com/tabibyte/session-notes) | `session-notes` | Create temporary one-off session notes |
| [Set View Mode per Note](https://github.com/yunidev-uk/obsidian-frontmatter-viewmode) | `frontmatter-viewmode` | Use YAML frontmatter to specify a view mode per note. |
| [Setlist.fm Sync](https://github.com/Fleker/setlist-for-obsidian) | `setlist-fm-sync` | Syncs your setlist.fm attended concerts. |
| [Sets](https://github.com/Canna71/obsidian-sets) | `sets` | Create, edit and search sets of notes like Notion or AnyType DBs |
| [Settings Management](https://github.com/xhuajin/obsidian-settings-management) | `settings-management` | Manage settings options, including show enabled/disabled plugins and css, grid layout, save current plugins/css enable config for quick enable/disable, etc. |
| [Settings profiles](https://github.com/4Source/settings-profiles-obsidian-plugin) | `settings-profiles` | Allows you to create various global settings profiles. You can sync them between different vaults. To keep all your settings in sync, you'll never have to manually adjust them again for every vault you have or create in the future. |
| [Settings Search](https://github.com/javalent/settings-search) | `settings-search` | Globally search settings in Obsidian.md |
| [ShaahMaat-md](https://github.com/MihailKovachev/shaahmaat-md) | `shaahmaat-md` | Render chess positions. |
| [Share as Gist](https://github.com/timrogers/obsidian-share-as-gist) | `obsidian-share-as-gist` | Shares an Obsidian note as a GitHub.com gist |
| [Share as ZIP](https://github.com/friebetill/obsidian-share-as-zip) | `share-as-zip` | Share notes and their links as a ZIP folder. |
| [Share my plugin list](https://github.com/Benature/obsidian-share-my-plugin-list) | `share-my-plugin-list` | Share the enabled plugins in list/table format. |
| [Share Note](https://github.com/alangrainger/share-note) | `share-note` | Instantly share a note, with the full theme and content exactly like you see in Reading View. Data is shared encrypted by default, and only you and the person you send it to have the key. |
| [Share to Cubox](https://github.com/Redwinam/obsidian-cubox) | `share-to-cubox` | Share Obsidian notes to Cubox. |
| [Share to Flomo](https://github.com/kaminono/obsidian-to-flomo) | `obsidian-to-flomo` | Quickly share content to Flomo. |
| [Share to NotionNext](https://github.com/jxpeng98/obsidian-to-NotionNext) | `share-to-notionnext` | Shares obsidian md file to notion with notion api for NotionNext web deploy, originally created by EasyChris/obsidian-to-notion. |
| [Share via Notepad Tab](https://github.com/revolter/obsidian-share-via-notepad-tab-plugin) | `share-via-notepad-tab` | Share notes via Notepad Tab (https://notepadtab.com). |
| [Sheet Plus](https://github.com/ljcoder2015/obsidian-sheet-plus) | `sheet-plus` | Create Excel-like spreadsheets and easily embed them in Markdown. |
| [Sheets Extended](https://github.com/NicoNekoru/obsidan-advanced-table-xt) | `sheets` | Vertical headers, merged cells, and custom css tables with advanced table compatibility |
| [Shell commands](https://github.com/Taitava/obsidian-shellcommands) | `obsidian-shellcommands` | You can predefine system commands that you want to run frequently, and assign hotkeys for them. For example open external applications. Automatic execution is also supported, and execution via URI links. |
| [Shell Path Copy](https://github.com/ckelsoe/obsidian-shell-path-copy) | `shell-path-copy` | Quickly copy vault file and folder paths for AI coding tools (Claude Code, Gemini CLI) - works on desktop and mobile with Windows/Unix formats |
| [Shiki Highlighter](https://github.com/mProjectsCode/obsidian-shiki-plugin) | `shiki-highlighter` | Highlight code blocks with Shiki. |
| [Shogi KIF Viewer](https://github.com/Luis8492/ShogiView) | `shogi-kif-viewer` | Render interactive shogi boards from KIF code blocks in notes. |
| [Short links](https://github.com/scottwillmoore/obsidian-short-links) | `short-internal-links-to-headings` | An Obsidian plugin to display short internal links. |
| [short tab name](https://github.com/Shumpei-Tanaka/obsidian-short-tab-name) | `short-tab-name` | set tab name to short for uid user |
| [Shortcut Launcher](https://github.com/macstories/obsidian-shortcut-launcher) | `obsidian-shortcut-launcher` | Trigger shortcuts in Apple's Shortcuts app from Obsidian with custom commands. |
| [Shortcuts extender](https://github.com/ryjjin/Obsidian-shortcuts-extender) | `shortcuts-extender` | Use shortcuts for text formatting or input special symbols without language switching |
| [Show Current File Path](https://github.com/ravimashru/obsidian-show-file-path) | `obsidian-show-file-path` | Show the full path of the currently open file in the status bar |
| [Show Diff](https://github.com/ivan-lednev/obsidian-automatic-changelog) | `show-diff` | Render Git diffs in Obsidian files |
| [Show Whitespace](https://github.com/ebullient/obsidian-show-whitespace-cm6) | `show-whitespace-cm6` | CSS styles and CM6 extensions to highlight whitespace in Source and Live Preview modes. |
| [Shrink pinned tabs](https://github.com/nicosomb/obsidian-shrink-pinned-tabs) | `shrink-pinned-tabs` | Shrinks pinned tabs to save screen space. |
| [Shukuchi](https://github.com/tadashi-aikawa/shukuchi) | `shukuchi` | Teleport to links (URL or internal link) and jump to their destinations. |
| [Sidebar Expand on Hover](https://github.com/toiq/obsidian-sidebar-expand-on-hover) | `obsidian-sidebar-expand-on-hover` | This Obsidian plugin expands or collapses the sidebars based on mouse hovering on the ribbons. |
| [Sidebar Highlights](https://github.com/trevware/obsidian-sidebar-highlights) | `sidebar-highlights` | View and manage text highlights, comments on highlights, native comments, and collections for your highlights. |
| [Sidebar Resizer](https://github.com/jeetsukumaran/obsidian-sidebar-resizer) | `sidebar-resizer` | Adjust the sidebar sizes easily. |
| [SideNote](https://github.com/mofukuru/SideNote) | `side-note` | Add comment on the part of sentence and refer in comment view. |
| [Sigma](https://github.com/monesga/obsidian-sigma) | `sigma` | A plugin to enable using obsidian notes as calculation sheets. |
| [Silicon AI](https://github.com/deepfates/silicon) | `silicon` | Add some intelligence to your notes with Silicon AI |
| [similar-notes](https://github.com/joybro/obsidian-similar-notes) | `similar-notes` |  |
| [Simple Anki Sync](https://github.com/lukmay/simple-anki-sync) | `simple-anki-sync` | The simplest way of syncing simple Flashchards with Anki. |
| [Simple Archiver](https://github.com/mfarr/obsidian-archive) | `simple-archiver` | Move old, stinky notes and folders to an archive, where they belong. |
| [Simple Banner](https://github.com/eatcodeplay/obsidian-simple-banner) | `simple-banner` | Visually enhance your notes with a customizable banner. Supports icons and time/date display. |
| [Simple CanvaSearch](https://github.com/ddalexb/obsidian-simple-canvasearch) | `simple-canvasearch` | Quickly fuzzy-search and shift focus to notes or cards within the currently opened canvas. |
| [Simple Citations](https://github.com/masaki39/simple-citations) | `simple-citations` | Add & update simple literature notes from Zotero. |
| [Simple Code Formatter](https://github.com/wiop93256/Simple-Code-Formmater) | `simple-code-formatter` | Format the code block where the cursor is. |
| [Simple Colored Folder](https://github.com/Mara-Li/obsidian-simple-colored-folder) | `simple-colored-folder` | Automagically add color to roots folders and customize them with Style Settings. |
| [Simple Columns](https://github.com/Josie1902/Simple-Columns) | `simple-columns` | Create and manage columns in your notes effortlessly, featuring customizable columns with easy-to-resize widths. |
| [Simple Dice Roller](https://github.com/yeeshue99/SimpleDiceRoller) | `simple-dice-roller` | A plug and play solution that allows you to average and simulate dice formulas. |
| [Simple Disguise](https://github.com/slow-groovin/simple-disguise) | `simple-disguise` | Disguise/obscure/hide the content in a very simple way. |
| [Simple File Info](https://github.com/lukas-cap/simple-file-info) | `simple-file-info` | A lightweight file info pane with native look and feel. |
| [Simple File Push](https://github.com/huedaya/obsidian-simple-file-push) | `simple-file-push` | Push Markdown file to API endpoint. |
| [Simple Focus](https://github.com/linqing24/obsidian-simple-focus) | `simple-focus` | Allows you to focus on a specific file or folder |
| [Simple Image Inserter](https://github.com/jdholtz/obsidian-image-inserter) | `simple-image-inserter` | Add images from the file system into Obsidian notes through a built-in file explorer. |
| [Simple Mention](https://github.com/der-tobi/obsidian-simple-mention) | `obsidian-simple-mention` | Get highlighted mentions and mention suggestions. Find all occurrences of a mention |
| [Simple Note Quiz](https://github.com/beginner137/Obsidian-simple-note-quiz) | `simple-note-quiz` | Start a simple quiz on your current note |
| [Simple Note Review](https://github.com/dartungar/obsidian-simple-note-review) | `simple-note-review` | Simple, customizable plugin for easy note review, resurfacing  & repetition. |
| [Simple Password](https://github.com/ShadiestGoat/obsidian-simple-password) | `simple-password` | Protect your vault behind a password |
| [Simple Prompt](https://github.com/arumie/obsidian-simple-prompt-plugin) | `simple-prompt` | Simple interface to generate or rewrite content using LLMs based on user input. |
| [Simple Quiz](https://github.com/IvanKalmar/simple-quiz) | `simple-quiz` | Creating simple quizzes. |
| [Simple RSS](https://github.com/monnierant/obsidian-simple-rss) | `simple-rss` | Collect RSS articles into notes. |
| [Simple Steam Auth](https://github.com/dreamscached/obsidian-simple-steam-auth) | `simple-steam-auth` | Generate Steam Guard codes right in your vault. |
| [Simple Tab Indent](https://github.com/hoomersinpsom/simple-tab-indent) | `simple-tab-indent` | Pressing Tab inserts a zero-width space + real tab, giving true indentation without triggering Markdown code blocks. Includes a settings panel to change the CSS tab width. |
| [Simple Table Math](https://github.com/eatcodeplay/obsidian-simple-table-math) | `simple-table-math` | Do some math (sum, average, etc.) in your markdown tables. |
| [Simple Todo](https://github.com/elliotxx/obsidian-simple-todo) | `simple-todo` | A minimalist text-based todo manager (Text-Based GTD) for efficient task management. |
| [Simple Vault Importer](https://github.com/WebInspectInc/obsidian-simple-template-importer) | `simple-vault-importer` | Import starter vaults into your own vault. |
| [simple-sketch](https://github.com/Yohh/obsidian-simple-sketch) | `simple-sketch` | Create minimalist sketches in a dedicated view, draw with a pencil, generate shapes, add text, save it to the vault or download it as an image. |
| [Simsapa](https://github.com/simsapa/simsapa-obsidian) | `simsapa` | Pāli dictionary and sutta search using Simsapa Dhamma Reader. Open a sidebar or double-click to lookup Pāli words in the dictionary, or search in the suttas. |
| [Single File Daily Notes](https://github.com/pranavmangal/obsidian-single-file-daily-notes) | `single-file-daily-notes` | Create and manage daily notes in a single file. |
| [Siteswap](https://github.com/tdresser/obsidian-siteswap) | `obsidian-siteswap` | Visualize Juggling Pattern Siteswap via the JugglingLab gif server. |
| [Size History](https://github.com/pbrw/obsidian-size-history) | `size-history` | Admire the growth of your Obsidian vault with a "hand-drawn" chart. |
| [Slackify Note](https://github.com/jeremyoverman/obsidian-slackify-note) | `slackify-note` | Converts a note to a Slack-compliant markdown using [slackify-markdown](https://www.npmjs.com/package/slackify-markdown) |
| [Slash Commander](https://github.com/alephpiece/obsidian-slash-commander) | `slash-commander` | Customize the slash command list, assign each command an icon. |
| [Slash snippets](https://github.com/echo-saurav/slash-snippets-plugin) | `slash-snippets` | Use slash command to insert quick text |
| [SlashComplete](https://github.com/Spiderpig86/slash-complete) | `slash-complete` | Adds Notion-style slash command autocompletion, enabling fast and intuitive insertion of Markdown blocks, formatting, and commands directly from the editor. This is a direct replacement for the default slash command plugin. |
| [Slide Note](https://github.com/Phantom1003/obsidian-slide-note) | `slide-note` | Conveniently take notes on PDF course slides :P |
| [Slides Extended](https://github.com/ebullient/obsidian-slides-extended) | `slides-extended` | Create markdown-based presentations using reveal.js |
| [Slurp](https://github.com/inhumantsar/slurp) | `slurp` | Slurps webpages and saves them as clean, uncluttered Markdown. |
| [Smart ChatGPT](https://github.com/brianpetro/smart-chatgpt-obsidian) | `smart-chatgpt` | Integrate OpenAI's ChatGPT seamlessly in notes. Automatically saves links, allows marking threads as done and integrates with Dataview. |
| [Smart Composer](https://github.com/glowingjade/obsidian-smart-composer) | `smart-composer` | AI chat with note context, smart writing assistance, and one-click edits for your vault. |
| [Smart Connections](https://github.com/brianpetro/obsidian-smart-connections) | `smart-connections` | Chat with your notes & see links to related content with Local or Remote models. |
| [Smart Connections Visualizer](https://github.com/Mossy1022/Smart-Connections-Visualizer) | `smart-connections-visualizer` | View your Smart Connections in a visualized format. |
| [Smart Context](https://github.com/brianpetro/smart-context-obsidian) | `smart-context` | Copy folder contents (Markdown & Canvas files) to the clipboard with a Smart Context approach. |
| [Smart DayNight switcher](https://github.com/Andrii256/ops_obsidian_smart-day-night-switcher) | `smart-day-night-switcher` | Intelligently determines sunrise and sunset times and automatically switches the color scheme to light or dark mode. |
| [Smart Export](https://github.com/LittleHaku/obsidian-smart-export) | `smart-export` | Plugin that follows wikilinks to a configurable depth, joining the notes into a single export. |
| [Smart HTML Select](https://github.com/IsaiaScope/smart-html-select-plugin) | `smart-html-select` | This plugin is useful to add an HTML select to your note with the possibility to configure the number of options. Integrates a logic behind the scene to change the markdown when in view mode the select value change. |
| [Smart Link Alias](https://github.com/vpcano/obsidian-smart-link-alias) | `smart-link-alias` | Enhance your internal links management with dynamic alias customization. Display short, full, or combined titles for your notes effortlessly. |
| [Smart Link Formatter](https://github.com/ccmdi/smart-link-formatter) | `smart-link-formatter` | Automatically fetches titles from pasted links, with additional customization for metadata from YouTube. |
| [Smart Links](https://github.com/kemayo/obsidian-smart-links) | `obsidian-smart-links` | This is a plugin for Obsidian that allows users to define custom link formats |
| [Smart Memos](https://github.com/Mossy1022/Smart-Memos) | `smart-memos` | Create personalized and intelligent analysis, summaries, and more for audio recordings that can be imported or spoken directly into a note |
| [Smart Random Note](https://github.com/erichalldev/obsidian-smart-random-note) | `smart-random-note` | A smart random note plugin |
| [Smart Rename](https://github.com/mnaoumov/obsidian-smart-rename) | `smart-rename` | Renames notes keeping previous title in existing links |
| [Smart Second Brain](https://github.com/your-papa/obsidian-Smart2Brain) | `smart-second-brain` | Interact with your privacy focused assistant, leveraging Ollama or OpenAI, making your second brain even smarter. |
| [Smart Templates](https://github.com/brianpetro/obsidian-smart-templates) | `smart-templates` | Build context-aware prompts from your existing Markdown templates and copy them into any AI chat. |
| [Smart Text Mover](https://github.com/Ankush-Chander/obsidian-smart-move-text) | `smart-text-mover` | Intelligent way to move text in file. |
| [Smart Title](https://github.com/maxzyma/obsidian-plugin-smart-title) | `smart-title` | Automatically extract tag and alias from the title. |
| [Smart Typography](https://github.com/mgmeyers/obsidian-smart-typography) | `obsidian-smart-typography` | Converts quotes to curly quotes, dashes to em dashes, and periods to ellipses |
| [Smart Vault Visualizer](https://github.com/Mossy1022/Smart-Connections-Vault-Visualizer) | `smart-vault-visualizer` | Visualizes and manages smart clusters and cluster groups in your vault. |
| [Smooth Cursor](https://github.com/busyoGG/SmoothCursor) | `smooth-cursor` | 平滑光标 Smooth Cursor |
| [Smooth Navigator](https://github.com/gasparschott/smooth-navigator) | `smooth-navigator` | Smoothly cycle through open files and splits via the keyboard. |
| [Smort](https://github.com/SmortApp/obsidian-smort) | `smort-obsidian` | Add Smort.io articles to Obsidian. Smort.io lets you easily edit, annotate and share articles. |
| [Snippet Commands](https://github.com/deathau/snippet-commands-obsidian) | `snippet-commands-obsidian` | Registers custom css snippets as commands (which you can bind hotkeys to) |
| [Snippetor](https://github.com/ebullient/obsidian-snippetor) | `obsidian-snippetor` | Create and tweak common snippets (starting with custom tasks) |
| [Snippets Manager](https://github.com/ramandv/obsidian-snippets-manager) | `snippets-manager` | A versatile text expansion plugin with full mobile support. Easily manage code snippets, personal info like passport numbers, email signatures, and more. Includes seamless Alfred integration and the ability to sync Awesome ChatGPT prompts as snippets. |
| [Snippets plugin](https://github.com/cristianvasquez/obsidian-snippets-plugin) | `snippets` | Execute simple scripts/snippets from obsidian. This plugin is experimental |
| [Snippetsaurus](https://github.com/Chrstn67/Snippetsaurus) | `obsnippets` | Create and managing text and code snippets. |
| [SOC Toolkit](https://github.com/michaelmassoni/obsidian-soc-toolkit) | `soc-toolkit` | A collection of tools for SOC analysts. |
| [SolidTime Integration](https://github.com/pronicx/obsidian-solidtime-integration) | `solidtime-integration` | Connect SolidTime to track your work time directly within your vault. |
| [Solo RPG Toolkit](https://github.com/alexkurowski/solo-toolkit) | `solo-rpg-toolkit` | Random generator tools geared towards solo TTRPG gameplay |
| [Solve](https://github.com/LiamRiddell/obsidian-solve) | `solve` | Supercharge your notes with real-time calculations without AI fuss. From dates ('Now + 20 days'), percentages ('10% of 120'), units of measurement ('100cm + 2m'), arithmetic ('10 + 5') and more! |
| [Song Links](https://github.com/Cutaiar/obsidian-song-links) | `spotify-links` | Insert a link to the song currently playing on your Spotify |
| [Sonkil](https://github.com/ohyoungpark/obsidian-sonkil) | `sonkil` | Provides Emacs-style text operations like Kill/Yank (Kill Ring), multi-cursor editing, and visual mark selection. |
| [Soomda](https://github.com/michaellee/soomda) | `obsidian-soomda` | Quickly hide your sidebars |
| [Sort & Permute lines](https://github.com/Vinzent03/obsidian-sort-and-permute-lines) | `obsidian-sort-and-permute-lines` |  |
| [Sort Frontmatter](https://github.com/mariomui/obsidian-sort-frontmatter) | `sort-frontmatter` | Sort frontmatter recursively |
| [Sortable Tables](https://github.com/filippov112/obsidian-sortable-tables) | `sortable-tables` | Adds sortable columns to markdown tables in preview mode. |
| [Soundscapes](https://github.com/andrewmcgivery/obsidian-soundscapes) | `soundscapes` | Adds a music/ambiance (E.g. lofi, white noise) player to the status bar to help with concentration. Also allows you to play your own local music files. |
| [Source Code Note](https://github.com/waiting0324/obsidian-code-note) | `source-code-note` | This plugin can help you organize source code note easily. |
| [Source Mode Styling](https://github.com/chrishoward-projects/sourcemode-styling) | `sourcemode-styling` | Provides a customisable raw look in source mode using a monospace font to clearly differentiate from Live Preview. |
| [Source Scanner](https://github.com/gerrie-myburgh/source-scanner) | `source-scanner` | Scan text source for comments then place it in vault as text files. |
| [Spaced everything](https://github.com/zachmueller/spaced-everything) | `spaced-everything` | Apply spaced repetition algorithms to everything in your vault. |
| [Spaced Repetition](https://github.com/st3v3nmw/obsidian-spaced-repetition) | `obsidian-spaced-repetition` | Fight the forgetting curve by reviewing flashcards & entire notes. |
| [Spaced Repetition AI](https://github.com/ai-learning-tools/obsidian-spaced-repetition-ai) | `spaced-repetition-ai` | Review, generate, and add flashcards for your notes using AI |
| [Spacekeys](https://github.com/jlumpe/obsidian-spacekeys) | `spacekeys` | Define hotkeys based on sequences of keypresses. |
| [Speech To Text Keyboard Helper](https://github.com/mwoz123/speech-to-text-keyboard-helper) | `speech2text-helper` | Makes available helper commands for Speech to Text (Google Andoroid) keyboard in Obsidian command pallete (and from there could be added to e.g. mobile buttons toolbar). |
| [Spellcheck Toggler](https://github.com/julzerinos/spellcheck-toggler-obsidian-plugin) | `spellcheck-toggler` | Toggle spellchecking for types of text blocks in the editing view. |
| [Spoiler Block](https://github.com/AllJavi/spoiler-block-obsidian) | `spoiler-block-obsidian` | Create Spoiler Blocks to hide information until you want to see it |
| [Spoilers](https://github.com/jacobtread/obsidian-spoilers) | `spoilers` | Hide and reveal blocks of information |
| [Spotify API](https://github.com/Darren-project/obsidian-spotify) | `spotify-api` | Exposes Spotify API |
| [Spotify Link](https://github.com/studiowebux/obsidian-spotify-link) | `spotify-link` | Include the song or podcast you're currently listening to in your note. |
| [Spreadsheets](https://github.com/divamgupta/obsidian-spreadsheets) | `spreadsheets` | Plugin to create spreadsheets in Obsidian. |
| [SQLite DB](https://github.com/stfrigerio/sqliteDB) | `sqlite-db` | Interact with local SQLite files in your notes |
| [SQLSeal](https://github.com/h-sphere/sql-seal) | `sqlseal` | Use SQL in your notes to query your vault files and CSV content. |
| [SQLSeal Charts](https://github.com/h-sphere/sql-seal-charts) | `sqlseal-charts` | Charts extension for SQLSeal plugin. Generate pie charts, bar charts, line charts and more using data stored in your vault! |
| [Squiggle](https://github.com/jqhoogland/obsidian-squiggle) | `squiggle` | Enables running squiggle code snippets within a note. |
| [Stack Overflow Answers](https://github.com/bramses/obsidian-stack-overflow) | `obsidian-stack-overflow` | Copy and Paste Stack Overflow answers directly into Obsidian. |
| [StandardForm](https://github.com/philphilphil/obsidian-standardform) | `standardform` | Transforms code blocks with Standard Form logical syntax into clean, styled renderings. Perfect for philosophy, logic, and argument reconstructions. |
| [Startpage](https://github.com/kuzzh/obsidian-startpage) | `start-page` | Automatically opens a customized homepage upon startup, displaying pinned and recent notes. |
| [Stashpad Docs](https://github.com/stashpad/obsidian-to-stashpad) | `stashpad-docs` | Create a Stashpad Doc from your notes. |
| [Statblock Sidekick](https://github.com/n21rl/stablock-sidekick) | `statblock-sidekick` | Create and expand D&D 5e statblocks. |
| [Static File Server](https://github.com/elias-sundqvist/obsidian-static-file-server) | `obsidian-static-file-server` | Host obsidian subfolders as static file servers. |
| [Static Site MD Exporter](https://github.com/yy4382/obsidian-static-site-export) | `ob2static-site` | Export specific notes to general md for static site generator like Hugo, Hexo, Astro and more. |
| [Status Bar Clock](https://github.com/marty331/status-bar-clock-obsidian) | `status-bar-clock` | Status bar clock. |
| [Status Bar Organizer](https://github.com/Opisek/obsidian-statusbar-organizer) | `statusbar-organizer` | Lets you rearrange and hide specific status bar elements. |
| [Status Bar Pomodoro Timer](https://github.com/kzhovn/statusbar-pomo-obsidian) | `obsidian-statusbar-pomo` | Adds a pomodoro timer to your status bar. |
| [Status Bar Quote](https://github.com/yesjinu/StatusBarQuote) | `status-bar-quote` | Show your favorite quote in obsidian status bar |
| [Steemit](https://github.com/anpigon/obsidian-steemit-plugin) | `obsidian-steemit` | A plugin for publishing Obsidian documents to Steemit. |
| [Stenography](https://github.com/bramses/stenography-obsidian) | `stenography-obsidian` | Auto Describe your code with machine learning using the Stenography API |
| [Steward](https://github.com/googlicius/obsidian-steward) | `steward` | An AI-powered assistant that helps you with your notes: Fast search, flexible commands, and chat with LLMs. |
| [Sticky Headings](https://github.com/imshenshen/obsidian-sticky-heading) | `sticky-heading` | Sticky Headings and Shows the heading level |
| [Sticky Notes](https://github.com/Abdo-reda/obsidian-sticky-notes-plugin) | `sticky-notes` | Create sticky notes popups. |
| [Stille](https://github.com/michaellee/stille) | `obsidian-stille` | Focus on your writing, a section at a time. |
| [Stopwatch Plugin](https://github.com/tokuhirom/obsidian-stopwatch-plugin) | `obsidian-stopwatch-plugin` | Display stopwatch on Obsidian! |
| [Storyclock Viewer](https://github.com/jonzfisher/obsidian-chronostory) | `storyclock` | Maps timing onto a storyclock. Inspired by Plot Devices Storyclock. |
| [Storyteller suite](https://github.com/Maws7140/obsidian-storyteller-suite) | `storyteller-suite` | World-building and story management — characters, locations, events, maps, compendium, timeline, manuscript compilation, and more. |
| [Strange New Worlds](https://github.com/TfTHacker/obsidian42-strange-new-worlds) | `obsidian42-strange-new-worlds` | Help see how your vault is interconnected with visual indicators. |
| [Strapi Exporter AI](https://github.com/CinquinAndy/notes-to-strapi-export-article-ai) | `notes-to-strapi-export-article-ai` | Effortlessly export your notes to Strapi CMS with AI-powered handling and SEO optimization. |
| [Strava Sync](https://github.com/watsonbox/obsidian-strava-sync) | `strava-sync` | Sync activities from Strava. |
| [Streams](https://github.com/bfloydd/streams) | `streams` | Create and manage multiple Daily Note streams. Stream <-> Daily Notes <-> Backlink. |
| [Strip Internal Links](https://github.com/adiron/obsidian-strip-internal-links) | `copy-without-links` | Strips the selection or current file of internal links and either copies to the clipboard, or in-place |
| [Structured](https://github.com/dobrovolsky/obsidian-structure) | `obsidian-structured-plugin` | Structured plugin. Create hierarchy in notes using . |
| [Structured Copy: Files & Folders](https://github.com/SeardnaSchmid/copy-recursive-content) | `copy-recursive-content` | Easily copy the contents of files and folders in a structured JSON format. |
| [Structured Tree](https://github.com/Rudtrack/structured-tree) | `structured-tree` | Explore, manage and navigate hierarchical notes |
| [Student Repo](https://github.com/yingflower/obsidian-stu-repo-helper) | `stu-repo-helper` | Manage student repositories. |
| [Style Importer](https://github.com/joshrouwhorst/style-importer) | `style-importer` | Import a stylesheet from a URL into your snippets folder. |
| [Style Settings](https://github.com/obsidian-community/obsidian-style-settings) | `obsidian-style-settings` | Offers controls for adjusting theme, plugin, and snippet CSS variables. |
| [Style Text](https://github.com/juanjoarranz/style-text-obsidian-plugin) | `style-text` | Apply custom CSS styles to selected text in your Obsidian Notes. |
| [Subdivider](https://github.com/MediosZ/obsidian-subdivider) | `subdivider` | Converts your notes into nested folders, automatically creating separate files for each subheading. |
| [Substitutions](https://github.com/BambusControl/obsidian-substitutions) | `substitutions` | Automatically replace text fragments with symbols or different text |
| [Suggest Notes](https://github.com/Doggy-Footprint/Suggest-Notes) | `suggest-notes` | Quick suggests for linkable notes |
| [Super Duper Audio Recorder](https://github.com/madpin/super-duper-audio-recorder) | `super-duper-audio-recorder` | Records audio directly, with input device and folder configuration, similar to the core one, but better |
| [Super Simple Time Tracker](https://github.com/Ellpeck/ObsidianSimpleTimeTracker) | `simple-time-tracker` | Multi-purpose time trackers for your notes! |
| [Supercharged Links](https://github.com/mdelobelle/obsidian_supercharged_links) | `supercharged-links-obsidian` | Add properties and menu options to links and style them! |
| [Superstition](https://github.com/shuxueshuxue/superstition) | `superstition` | Manage routines with traditional calendar concept of 宜/忌 |
| [SupSub](https://github.com/wjgoarxiv/obsidian-supsub) | `supsub` | `Supsub` is a plugin designed for Obsidian.md that adds functionality to wrap selected text with <sup></sup> (superscript) or <sub></sub> (subscript) tags. |
| [Surfing](https://github.com/PKM-er/Obsidian-Surfing) | `surfing` | Surf the Net in Obsidian. |
| [Svelte Syntax Highlighter](https://github.com/typhoon-kim/obsidian-svelte-syntax-highlighter) | `svelte-syntax-highlighter` | Syntax highlighting for Svelte code blocks. |
| [SVG Style Editor](https://github.com/arg1998/obsidian-svg-styler) | `svg-styler` | Change the color and other style properies of an embded SVG file |
| [SwiftLaTeX Render](https://github.com/gboyd068/obsidian-swiftlatex-render) | `swiftlatex-render` | Render LaTeX in codeblocks into pdf or svg, without needing to install LaTeX separately. |
| [Swiss army knife](https://github.com/mwoz123/swiss-army-knife-obsidian) | `swiss-army-knife` | Collection of various utilities e.g. duplicate empty line remove, create expandable/colapsable sections, Obsidian plugin release/tag version download (eg. for mobile tests) |
| [Symbol linking](https://github.com/Mara-Li/obsidian-symbol-linking) | `symbol-linking` | Adds ability to link with any trigger. Each trigger can limit linking to specific folders or file. |
| [Symbols Prettifier](https://github.com/FlorianWoelki/obsidian-symbols-prettifier) | `symbols-prettifier` | This plugin allows you to prettify the symbols with actual symbols you commonly type, like arrows. |
| [Symlink Creator](https://github.com/pteridin/obsidian_symlink_plugin) | `symlink-creator` | Create symlinks to files and folders inside and outside of your vault. |
| [Synaptic Bridge](https://github.com/especialkim/synaptic-bridge) | `markdown-hijacker` | Beyond the Vault. One hub for every Markdown, everywhere |
| [Synaptic View](https://github.com/especialkim/obsidian-synaptic-view) | `synaptic-view` | A dynamic control center for your vault. Unify hubs, notes, tasks, periodic notes, and web resources with intuitive buttons. Replace new tab for instant access. |
| [Sync Cnblog](https://github.com/lei-ctyh/obsidian-sync-cnblog) | `sync-cnblog` | 将笔记同步到博客园 |
| [Sync config folder to common folder](https://github.com/codeonquer/obsidian-sync-config-folder-to-common-folder) | `sync-config-folder-to-common-folder` | Sync contents from config folder to common folder for backup or other purposes |
| [Sync Contacts on macOS](https://github.com/motschel123/Mac-Contact-Sync-Obsidian) | `sync-contacts-macos` | Sync your contacts from macOS to your Obsidian Vault. |
| [Sync Google Calendar](https://github.com/dexin-qi/obsidian-sync-calendar) | `sync-google-calendar` | Synchronize events from Google Calendar and manage them like tasks. |
| [Sync Graph Settings](https://github.com/Xallt/sync-graph-settings) | `sync-graph-settings` | This is a plugin for syncing various graph settings to Local Graphs |
| [Sync Vault](https://github.com/abcamus/obsidian-sync-vault-ce) | `sync-vault-ce` | Professional cloud sync & VFS for Obsidian. Features zero-space VFS, 4K streaming, MCP AI engine, and P2P collaboration. Supports Baidu/Aliyun/Quark/WebDAV/S3. |
| [sync-db-os](https://github.com/ketd/obsidian-sync-DB-OS) | `sync-db-os` | For synchronization between multiple platforms |
| [Sync-safe file names](https://github.com/j-maas/sync-safe-file-names) | `sync-safe-file-names` | Ensures all file names can be synced accross all platforms. |
| [sync-to-xlog](https://github.com/Otto-J/sync-to-xlog) | `sync-to-xlog` | Publish your obsidian file to xlog.app |
| [SyncFTP](https://github.com/alex-donnan/SyncFTP) | `syncftp` | This plugin syncs files to an SFTP, with credentials in settings. |
| [syncread-assistant](https://github.com/flyer1b/LightRead-master) | `syncread` | sync articles from syncread app |
| [Syncthing Integration](https://github.com/LBF38/obsidian-syncthing-integration) | `syncthing-integration` | Integrates most of Syncthing features into Obsidian. |
| [Syncthing status icon](https://github.com/Diego-Viero/Syncthing-status-icon-Obsidian-plugin) | `syncthing-status-icon` | Adds an icon in the status bar displaying Syncthing sync status. It shows a red circle if disconnected, green if connected, and yellow if scanning, not fully synced, or no device is connected. Provides detailed file completion and unsynced file counts, with a hover widget and custom view for more information. |
| [Syrinscape Online Player](https://github.com/scooper4711/obsidian-syrinscape) | `syrinscape-player-control` | Control Syrinscape Online Player from inside of notes. |
| [SystemSculpt AI](https://github.com/SystemSculpt/obsidian-systemsculpt-ai) | `systemsculpt-ai` | A powerful AI that helps you sculpt your knowledge base with artificial intelligence through intelligent chat, document analysis, and seamless integrations. |
| [T4: Task Tree Time Totaler](https://github.com/estory1/t4-task-tree-time-totaler) | `t4-task-tree-time-totaler` | Calculates and assigns task estimates given subtask estimates in a task tree in a Markdown document. |
| [Tab File Path](https://github.com/johnburnett/obsidian-tab-file-path) | `tab-file-path` | Shows file paths in tabs |
| [Tab Group Arrangement](https://github.com/situ2001/obsidian-tab-group-arrangement) | `tab-group-arrangement` | Arrange the tab group in a more flexible way. For now, it supports arranging evenly and expanded like VSCode. User can make action and switch mode of arrangement by clicking the status bar or executing commands. |
| [Tab Limiter](https://github.com/lizard-heart/obsidian-tab-limit) | `tab-limit` | Limits the number of tabs that can be opened. |
| [Tab Navigator](https://github.com/o02c/obsidian-tab-navigator) | `tab-navigator` | Simple Tab Switcher, search open tabs. |
| [Tab Panels](https://github.com/GnoxNahte/obsidian-tab-panels) | `tab-panels` | Create tab panels to organize content into sections |
| [Tab Rotator](https://github.com/autohub7/obsidian-tab-rotator) | `tab-rotator` | This plugin rotates opened files to the left or right with a specified interval |
| [Tab Selector](https://github.com/namikaze-40p/obsidian-tab-selector) | `tab-selector` | Quickly switch tabs in various ways. |
| [Tab Shifter](https://github.com/jsrozner/obsidian-tab-shifter) | `tab-shifter` | Enables shifting tabs between different tab splits and some other basic IDE tab functionalities |
| [Tab Switcher](https://github.com/Vinzent03/tab-switcher) | `cycle-through-panes` | Switch your tabs with Ctrl + Tab in recently used order like in a browser. |
| [Table Checkbox Renderer](https://github.com/dannns/obsidian-table-checkbox-renderer) | `table-checkbox-renderer` | Interactive checkboxes for Markdown tables. Toggle checkboxes in Reading Mode to instantly update the Markdown file. Supports multiple checkboxes per cell and any table layout. |
| [Table Extended](https://github.com/aidenlx/table-extended) | `table-extended` | Enable extended table support with MultiMarkdown 6 syntax |
| [Table Generator](https://github.com/Quorafind/Obsidian-Table-Generator) | `obsidian-table-generator` | A plugin for generate markdown table quickly like Typora /card table in canvas . |
| [Table List](https://github.com/Akaswan/table-list) | `table-list` | Adds a table view to manage your tasks. |
| [Table of Contents](https://github.com/hipstersmoothie/obsidian-plugin-toc) | `obsidian-plugin-toc` | Create a table of contents for a note. |
| [Table to CSV Exporter](https://github.com/metawops/obsidian-table-to-csv-export) | `obsidian-table-to-csv-exporter` | This plugin allows for exporting tables from a pane in reading mode into CSV files. |
| [Tabout](https://github.com/phibr0/obsidian-tabout) | `tabout` | Easily "tab out" of Links or other Markdown Formatting Characters. |
| [Tabs](https://github.com/xhuajin/obsidian-tabs) | `tabs` | Create tabs in your notes. |
| [Tag & Word Cloud](https://github.com/joethei/obsidian-tagcloud) | `tag-word-cloud` | Show a cloud of your tags/words in a note |
| [Tag Breakdown Generator](https://github.com/HananoshikaYomaru/obsidian-tag-generator) | `tag-breakdown-generator` | Breakdown nested tags into multiple parent tags |
| [Tag Buddy](https://github.com/moremeyou/Obsidian-Tag-Buddy) | `tag-buddy` | Unlock powerful tag editing features in Reading Mode. Add, remove, and edit tags across your vault, in the active note or a single instance. Use tag summaries to roundup and process tagged content like an inbox. |
| [Tag Formatter](https://github.com/snsvrno/snsvrno-short-tags) | `snsvrno-tags` | Gives more options on how to display tags in preview mode. |
| [Tag Group Manager](https://github.com/Stargazer-cc/obsidian-tag-group-manager) | `tag-group-manager` | Manage tag groups and quickly insert tags. |
| [Tag Index](https://github.com/wenlzhang/obsidian-tag-index) | `tag-index` | Create a curated list of important tags to serve as meaningful entry points to your knowledge base. |
| [Tag Links](https://github.com/zedseven/obsidian-tag-links) | `tag-links` | Allows tags to be opened as links using a hotkey. |
| [Tag Page](https://github.com/mjsumpter/obsidian-tag-page) | `tag-page-md` | Dynamically generate and update tag-specific pages, offering a consolidated view of each tag's references across your vault. |
| [Tag Project](https://github.com/Odaimoko/tag-project) | `tag-project-odaimoko` | A Project Management Tool: Tag tasks everywhere, Manage in One page. |
| [Tag Summary](https://github.com/macrojd/tag-summary) | `tag-summary-plugin` | This plugin creates summaries with paragraphs or blocks of text that share the same tag(s). |
| [Tag Tactician](https://github.com/scottTomaszewski/obsidian-tag-tactician) | `tag-tactician` | Better tag management: Bulk operations, navigation by tags, and find related notes through tag similarity |
| [Tag Timer](https://github.com/quantavil/Tag-Timer) | `tag-timer` | Add inline timers to any line in your notes. |
| [Tag Wrangler](https://github.com/pjeby/tag-wrangler) | `tag-wrangler` | Rename, merge, toggle, and search tags from the tags view |
| [TagFolder](https://github.com/vrtmrz/obsidian-tagfolder) | `obsidian-tagfolder` | Show tags as folder |
| [Tagged Documents Viewer](https://github.com/mgeduld/obsidian-tagged-documents-viewer) | `obsidian-plugin-tagged-documents-viewer` | Opens a modal with scrollable content of all documents that contain a specific tag or tags. |
| [TagMany](https://github.com/joshua-martius/tagmany) | `tag-many` | Add the same tag(s) to multiple notes in a folder (optionally including subfolders) at once. |
| [Tags for Markdown](https://github.com/binarynoir/obsidian-markdown-tags) | `markdown-tags` | Enhance your documents with custom tags. Use predefined or custom labels, customizable colors, and arrow indicators to visually track tasks and statuses. |
| [Tags Overview](https://github.com/christianwannerstedt/obsidian-tags-overview) | `tags-overview` | Adds an extended tags panel where tagged files can be overviewed, filtered and accessed in an easy way. |
| [Tags Routes](https://github.com/kctekn/obsidian-TagsRoutes) | `tags-routes` | A powerful 3D graph visualization tool offers dynamic time-lapse, intelligent orphan file management, tag-based queries, and a range of displaying customization options for a great insightful experience. |
| [Tagvis](https://github.com/mason-bryant/Obsidian-Tagvis) | `d3-tagvis` | Tag visualization for those that are into that kind of thing. |
| [Tailwind Snippet](https://github.com/nicholas-wilcox/tailwind-snippet-obsidian-plugin) | `tailwind-snippet` | Use TailwindCSS utility classes in your markup. |
| [Target Word Count](https://github.com/twofive-labs/target-word-count) | `target-word-count` | Disable editing until you've added a target number of words. |
| [Tars](https://github.com/TarsLab/obsidian-tars) | `tars` | Text generation based on tag suggestions, using DeepSeek, Claude, OpenAI, OpenRouter, SiliconFlow, Gemini, Qwen & more. |
| [Task Board](https://github.com/tu2-atmanand/Task-Board) | `task-board` | Manage all your tasks throughout your vault from a single board and much more... |
| [Task Collector (TC)](https://github.com/ebullient/obsidian-task-collector) | `obsidian-task-collector` | Change task status and collect tasks within a document using hotkeys and context menus. |
| [Task Director](https://github.com/cybertramp/obsidian-task-director) | `task-director` | Manage and change tasks targeting a specific page |
| [Task Genius](https://github.com/taskgenius/taskgenius-plugin) | `obsidian-task-progress-bar` | Comprehensive task management that includes progress bars, task status cycling, and advanced task tracking features. |
| [Task list](https://github.com/ted-marozzi/task-list) | `task-list` | Enable better task management via lists. |
| [Task List Kanban](https://github.com/ErikaRS/task-list-kanban) | `task-list-kanban` | Organizes all of the tasks within your files into a kanban view. Reduce duplication of effort when managing and prioritising tasks by simply using the task format in your files to automatically appear in your Task List Kanban. |
| [Task Marker](https://github.com/wenlzhang/obsidian-task-marker) | `obsidian-task-marker` | Change task statuses with hotkeys and context menu. Complete, cancel and mark tasks, as well as cycle among selected task statuses. |
| [Task Mover](https://github.com/nemariia/task-mover) | `task-mover` | A plugin to move unfinished tasks to the daily note automatically |
| [Task Status](https://github.com/vburzynski/obsidian-task-status) | `task-status` | Quickly select and apply custom task status markers |
| [Taskbone](https://github.com/schlundd/obsidian-ocr-plugin) | `taskbone-ocr-plugin` | Sync Obsidian with Todoist, extract text from images (OCR). |
| [TaskNotes](https://github.com/callumalpass/tasknotes) | `tasknotes` | Note-based task management with calendar, pomodoro and time-tracking integration. |
| [Tasks](https://github.com/obsidian-tasks-group/obsidian-tasks) | `obsidian-tasks-plugin` | Track tasks across your vault. Supports due dates, recurring tasks, done dates, sub-set of checklist items, and filtering. |
| [Tasks Calendar Wrapper](https://github.com/Leonezz/obsidian-tasks-calendar-wrapper) | `tasks-calendar-wrapper` | This is a simple wrapper for Obsidian-Tasks-Calendar (https://github.com/702573N/Obsidian-Tasks-Calendar) and Obsidian-Tasks-Timeline (https://github.com/702573N/Obsidian-Tasks-Timeline). |
| [Tasks Cleaner](https://github.com/lowitea/obsidian-tasks-cleaner) | `tasks-cleaner` | Find and remove outdated tasks. |
| [Tasks Map](https://github.com/NicoKNL/tasks-map) | `tasks-map` | A graph view of your tasks. |
| [TaskWarrior Task Wiki](https://github.com/SntTGR/obsidian-tw-task-wiki) | `tw-task-wiki` | Wrapper and integration around TaskWarrior. Allows you to view and edit tasks in your TaskWarrior database as tables. |
| [Tekken Notation](https://github.com/OpTi9/obsidian-tekken-notation) | `tekken-notation` | Renders Tekken Notation. |
| [Telegram Inbox](https://github.com/icealtria/obsidian-telegram-inbox) | `telegram-inbox` | Receive messages from Telegram bot and add them to daily note. |
| [Telegram Sync](https://github.com/soberhacker/obsidian-telegram-sync) | `telegram-sync` | Transfer messages and files from Telegram to Obsidian. |
| [Telegraph Publish](https://github.com/reorx/obsidian-telegraph-publish) | `obsidian-telegraph-publish` |  |
| [Teleprompter](https://github.com/lumetrium/obsidian-teleprompter) | `teleprompter` | Teleprompter window for live presentations and video production. |
| [Template by Note Name](https://github.com/jacoblearned/obsidian-template-by-note-name) | `template-by-note-name` | Automatically template notes based on their title. |
| [Template Filename](https://github.com/callumalpass/obsidian-template-filename) | `template-filename` | Create notes with templatable filenames, using date/time formats, random strings, and custom base numbering systems. |
| [Template Folder](https://github.com/LucasOe/obsidian-template-folder) | `template-folder` | Moves notes to a folder when applying a template. |
| [Templated daily notes](https://github.com/digitorum/obsidian-templayted-daily-notes) | `templated-daily-notes` | Adds the ability to create daily notes with a specified template according to the described settings |
| [Templater](https://github.com/SilentVoid13/Templater) | `templater-obsidian` | Create and use templates |
| [Templify](https://github.com/Quorafind/Obsidian-Templify) | `templify` | (Closed Source) Multi layout for one note. |
| [Tencent COS for Imgur](https://github.com/bobostudio/obsidian-imgur-plugin) | `imgur-tencent-cos` | Upload images to Tencent COS for Imgur. |
| [Tengwar](https://github.com/mikevetkin/obsidian-tengwar) | `tengwar` | Support Tengwar (The Elvish Letters) |
| [Tenki](https://github.com/ms3056/Tenki) | `tenki` | Display the weather. |
| [Terminal](https://github.com/polyipseity/obsidian-terminal) | `terminal` | Integrate consoles, shells, and terminals. |
| [Testing Vault](https://github.com/pedersen/obsidian-testing-vault) | `testing-vault` | This allows a developer to make a random vault of arbitrary size for testing their plugins. |
| [Text Analysis](https://github.com/mihakralj/obsidian-textanalysis) | `textanalysis` | Real-time text analysis on readability, structure, and complexity, incorporating over 30 tests like Average Syllables per Word, percent of difficult words, Lexical Diversity, Flesch Reading Ease Score, Gunning Fog Index, SMOG indes, Rix, Lix, Reading level and Reading/Speaking time. Built on top of textstat library. |
| [Text Autocomplete](https://github.com/c-degni/text-autocomplete) | `text-autocomplete` | Autocomplete text to type more efficiently. |
| [Text Block Timer](https://github.com/wth461694678/text-block-timer) | `text-block-timer` | Add a timer to text block to enable count-up timing (Performance Improved!). |
| [Text Conversions](https://github.com/ironsigma/obsidian-text-conversions) | `text-conversions` | Perform various text conversions on the selected text |
| [Text expand](https://github.com/mrjackphil/obsidian-text-expand) | `mrj-text-expand` | Search and paste/transclude links to located files. |
| [Text Extractor](https://github.com/scambier/obsidian-text-extractor) | `text-extractor` | A (companion) plugin to facilitate the extraction of text from images (OCR) and PDFs. |
| [Text Finder](https://github.com/nyable/obsidian-text-finder) | `text-finder` | Provides a find/replace window in edit mode similar to VSCode (supports regular expressions and case sensitivity). |
| [Text Focus](https://github.com/usysrc/obsidian-text-focus-plugin) | `text-focus` | Focus the text area when creating new notes. |
| [Text Format](https://github.com/Benature/obsidian-text-format) | `obsidian-text-format` | Format text such as lowercase/uppercase/capitalize/titlecase, converting order/bullet list, removing redundant spaces/newline characters. |
| [Text Generator](https://github.com/nhaouari/obsidian-textgenerator-plugin) | `obsidian-textgenerator-plugin` | Text generation using AI |
| [Text Progress Bar](https://github.com/michaeladams/obsidian-text-progress-bar) | `text-progress-bar` | Display low-fi text progress bars in your notes. |
| [Text Snippets](https://github.com/ArianaKhit/text-snippets-obsidian) | `text-snippets-obsidian` | Allows you to replace text templates for faster typing, create your own, expand text shortcuts. |
| [Text to Speech](https://github.com/joethei/obsidian-tts) | `obsidian-tts` | Hear your notes. |
| [Text Transform](https://github.com/ipshing/obsidian-text-transform) | `text-transform` | Transform text to different cases using the command palette or keyboard shortcuts. |
| [Text Transporter](https://github.com/TfTHacker/obsidian42-text-transporter) | `obsidian42-text-transporter` | Advanced text tools for working with text in your vault |
| [Text Wrapper](https://github.com/smx0/obs-text-wrapper) | `obs-text-wrapper` | Quickly wrap selected text with HTML tags by using a shortcut or from the command palette |
| [text2anki-openai](https://github.com/manibatra/obsidian-text2anki-openai) | `text2anki-openai` | This is an obsidian plugin that uses OpenAI to generate flashcards from text and add them to Anki. |
| [Text2Audio](https://github.com/luhaifeng666/obsidian-text2audio) | `text2audio` | Convert text to speech |
| [Textfresser](https://github.com/clockblocker/filler-de) | `cbcr-text-eater-de` | Go trough the german texts and build your own dictionary based on your own unique contexts |
| [Textgrams](https://github.com/akopdev/obsidian-textgrams) | `textgrams` | Store and visualise ASCII graphics and charts |
| [Tezcat](https://github.com/mmargenot/tezcat) | `tezcat` | Implements AI indexing and search to surface related thoughts to your current work. Look into the mirror. |
| [TG Emoji Search](https://github.com/MarsBatya/tg-emoji-search) | `tg-emoji-search` | Lets you type out emojis like in Telegram. |
| [The One Ring 2E Statblocks](https://github.com/modality/obsidian-the-one-ring-2e-statblocks) | `tor2e-statblocks` | Render TOR 2e statblocks in Obsidian. |
| [The Queue](https://github.com/koljapluemer/obsidian-the-queue) | `the-queue` | Randomly exposes you to notes from your vault. Supports habits, to-dos, spaced repetition flashcards, iterative reading and more. |
| [The Spirit's Book](https://github.com/ahlrodrigues/spirits-book) | `spirits-book` | Plugin to study and explore *The Spirit's Book* by Allan Kardec, directly within your vault. |
| [Thecap cv generator](https://github.com/xthecapx/Thecap-cv-generator) | `thecap-cv-generator` | Generate PDF curriculum from your notes. |
| [Theme by Folder](https://github.com/JinmuGo/obsidian-theme-by-folder) | `theme-by-folder` | Automatically switch themes based on the folder of the opened note |
| [Theme Controller](https://github.com/Binaris00/Theme-Controller) | `bin-theme-controller` | Set when and how the themes will be displayed. |
| [Theme Design Utilities](https://github.com/chrisgrieser/obsidian-theme-design-utilities) | `obsidian-theme-design-utilities` | Some utilities and Quality-of-Life features for designers of Obsidian themes. |
| [Theme Picker](https://github.com/trey-sedate/obsidian-theme-picker) | `theme-picker` | Quickly preview installed themes |
| [Theme toggle](https://github.com/gapmiss/theme-toggle) | `theme-toggle` | Dark/light theme toggle via ribbon icon or command |
| [Theme Toggler](https://github.com/larsmagnus/obsidian-theme-toggler) | `obsidian-theme-toggler` | Toggle the theme in Obsidian's panels. |
| [Themed Discord RPC](https://github.com/Mouadhbendjedidi/themed-obsidian-discord-rpc) | `themed-discord-rpc` | A Customizable Discord RPC |
| [Things Link](https://github.com/gavinmn/obsidian-things-link) | `obsidian-things-link` | Seamlessly create Things tasks and projects from Obsidian |
| [Things Logbook](https://github.com/liamcain/obsidian-things-logbook) | `things-logbook` | Sync your Things.app Logbook with daily notes |
| [Things3 Sync](https://github.com/royxue/obsidian-things3-sync) | `obsidian-things3-sync` | An Obsidian plugin for sync between Obsidian and Things3, create Todo and sync Todo status |
| [Things3 Today](https://github.com/wudanyang6/obsidian-things3-today) | `things3-today` | Manage today's tasks with Things3 |
| [Thino](https://github.com/Quorafind/Obsidian-Thino) | `obsidian-memos` | Capturing ideas and save them into daily notes. (Closed source) |
| [Three Noun Prompts](https://github.com/jamespeachh/Three-Noun-Prompts) | `three-noun-prompts` | Use TOPT algorithm to get daily writing prompts! |
| [Thumbnails](https://github.com/Meikul/obsidian-thumbnails) | `obsidian-thumbnails` | Insert video thumbnails into your notes |
| [Tick Tones](https://github.com/DontBlameMe99/Tick-Tones) | `tick-tones` | Plays a tone when you tick a checkbox |
| [TickTick](https://github.com/viduycheung/ticktick-obsidian) | `ticktick` | Check and create tasks in TickTick via Obsidian |
| [TickTick Quick Add Task](https://github.com/muxinli/ticktick-quick-add-obsidian) | `ticktick-quickadd-task` | Create TickTick tasks from text blocks with automatic Obsidian URI links. Requires Advanced URI plugin. |
| [TickTickSync](https://github.com/thesamim/TickTickSync) | `tickticksync` | Sync TickTick tasks to Obsidian, and Obsidian tasks to TickTick |
| [tidit](https://github.com/codingthings-com/tidit-obsidian) | `tidit` | tidit adds timestamps to your document as you type — when you want it, how you want it, where you want it. |
| [Tidy Footnotes](https://github.com/charliecm/obsidian-tidy-footnotes) | `obsidian-tidy-footnotes` | Tidy your footnotes seamlessly. |
| [Tier List](https://github.com/MoxAlehin/TierList) | `tier-list` | Visual ranking and organizing content into customizable tier lists. |
| [Tiff Viewer](https://github.com/ullmannJan/obsidian-tiff-viewer) | `tiff-viewer` | View .tif(f) files by generating duplicates in form of .tif(f).png |
| [TikToker](https://github.com/ameyxd/obsidian-tiktoker) | `tiktoker` | Save TikTok videos as markdown notes with embedded content and metadata extraction. |
| [TikZJax](https://github.com/artisticat1/obsidian-tikzjax) | `obsidian-tikzjax` | Render LaTeX and TikZ diagrams in your notes |
| [Time Bullet](https://github.com/pedrogdn/obsidian-time-bullet-plugin) | `time-bullet` | Quickly add timestamp bullet points to your notes |
| [Time Inserter](https://github.com/heycalmdown/obsidian-time-inserter) | `time-inserter` | Insert current time at cursor position, rounded to nearest 5-minute interval. |
| [Time Ruler](https://github.com/j-palindrome/obsidian-time-ruler) | `time-ruler` | A drag-and-drop time ruler combining the best of a task list and a calendar view (integrates with Tasks, Full Calendar, and Dataview). |
| [Time Things](https://github.com/plasmabit/timethings) | `timethings` | Show clock in the corner. Track total editing time of a note and the last time it was modified. |
| [Timecodes](https://github.com/gavvvr/obsidian-timecodes-plugin) | `timecodes` | Converts raw text timecodes into clickable URLs if a note contains a link to a video |
| [TimeDiff](https://github.com/dominiczaq/obsidian-plugin-time-diff) | `obsidian-plugin-time-diff` | Plugin which calculates and displays diff in hours and minutes between two dates in `timediff` markdown block |
| [Timekeep](https://github.com/jacobtread/obsidian-timekeep) | `timekeep` | Time tracking |
| [Timeline](https://github.com/George-debug/obsidian-timeline) | `obsidian-timeline` | Used to build great timelines |
| [Timeline Canvas Creator](https://github.com/chris-codes1/timeline-canvas-creator) | `timeline-canvas-creator` | Quickly create timeline structured canvases. |
| [Timeline Schedule](https://github.com/Ebonsignori/obsidian-timeline-schedule) | `timeline-schedule` | Inline timelines generated from human-readable time strings, e.g. 'Walk dog (30min)' in a ```schedule codeblock. |
| [Timeline View](https://github.com/b-camphart/timeline-view) | `timeline-view` | Display your obsidian notes in a timeline, based on a given property. |
| [Timelines (Revamped)](https://github.com/seanlowe/obsidian-timelines) | `timelines-revamped` | Successor to darakah's Timelines plugin: Generate a chronological timeline in which all 'events' are notes that include a specific tag or set of tags. |
| [Timelive](https://github.com/aNNiMON/obsidian-timelive) | `timelive` | Turn a list of dates into a timeline. |
| [Timelog](https://github.com/eddie/obsidian-time-log) | `time-log` | Add timestamps to entries under dated headers for lab notebook style logging. |
| [Timer](https://github.com/Raboro/obsidian-timer-plugin) | `timer` | Allows you to measure time. |
| [TimeSaver](https://github.com/odayou/task-processing-extension) | `time-saver` | Save your time. 1. Quickly insert todo directive. 2. Quickly count the time spent on tasks in the current note and the total time spent. |
| [Timesheet](https://github.com/vkostyanetsky/ObsidianTimesheet) | `timesheet` | Timesheet generator for tasks in daily notes. |
| [Timestamp Link](https://github.com/wenlzhang/obsidian-timestamp-link) | `timestamp-link` | Copy timestamped links to blocks, headings and notes. |
| [Timestamp Notes](https://github.com/juliang22/ObsidianTimestampNotes) | `obsidian-timestamp-notes` | This plugin allows side-by-side notetaking with videos. Annotate your notes with timestamps to directly control the video and remember where each note comes from. |
| [TimeStamper](https://github.com/Gru80/obsidian-timestamper) | `obsidian-timestamper` | Insert customized time/date stamp. |
| [Timestamper](https://github.com/coignard/obsidian-timestamper) | `timestamper` | Insert the current timestamp into your notes. |
| [Timetracker](https://github.com/hedgehog1833/obsidian-timetracker) | `timetracker` | Adds a stopwatch whose value can be inserted in the editor per hotkey. |
| [Tiny Habits](https://github.com/nazoadiego/tiny-habits) | `tiny-habits` | Habit tracking table for your markdown notes |
| [TinyChart](https://github.com/alincoop/obsidian-tinychart) | `tinychart` | Dead simple ASCII charts |
| [TinyPNG Image](https://github.com/ckt1031/obsidian-tinypng-plugin) | `tinypng-image` | Compress images using TinyPNG to save your storage. |
| [TIPA Support](https://github.com/akdemirdeniz/obsidian-tipa) | `tipa-support` | Adds support for TIPA phonetic notation. |
| [Title As Link Text](https://github.com/lextoumbourou/obsidian-title-as-link-text) | `title-as-link-text` | Automatically updates link text to use note titles instead of filenames. |
| [Title Generator](https://github.com/jaschaephraim/obsidian-title-generator) | `title-generator` | Quickly and easily title your notes using OpenAI's GPT-3.5 |
| [Title renamer](https://github.com/stroiman/obsidian-title-sync) | `title-renamer` | Synchronise title in markdown when file is renamed. |
| [Title Serial Number Plugin](https://github.com/yalvhe2009/obsidian-title-serial-number-plugin) | `obsidian-title-serial-number-plugin` | This plugin adds serial numbers to your markdown title. |
| [Title-Only Tab](https://github.com/tristone13th/obsidian-title-only-tab) | `title-only-tab` | Set tab name to title in frontmatter for Jekyll users |
| [tldraw](https://github.com/tldraw/obsidian-plugin) | `tldraw` | Create whiteboards, diagrams, and drawings with the official tldraw plugin. |
| [TOC compatible with Publish](https://github.com/BrMacCath/Table-of-Contents) | `table-of-contents-automatic-but-compatible-with-publish` | Create table of contents with user defined adjustments. All adjustments will be compatible with Obsidian Publish. |
| [TODO Highlighter](https://github.com/heavenlygaze/obsidian-todo-highlighter) | `todo-highlighter` | Highlights TODO regex as green. |
| [Todo sort](https://github.com/ryangomba/obsidian-todo-sort) | `todo-sort` | A plugin for Obsidian (https://obsidian.md) that sorts todos by completion status. |
| [TODO Wrangler](https://github.com/Jeel-Shah/todo-wrangler) | `wrangle-todos` | Wrangles your TODOs and puts them at the bottom of the file. |
| [TODO | Text-based GTD](https://github.com/larslockefeer/obsidian-plugin-todo) | `obsidian-plugin-todo` | Text-based GTD in Obsidian. Collects all outstanding TODOs from your vault and presents them in lists Today, Scheduled, Inbox and Someday/Maybe. |
| [Todo.txt Mode](https://github.com/rioskit/obsidian-todo-txt-mode) | `todo-txt-mode` | Support for todo.txt file format with syntax highlighting and task management |
| [Todoist completed tasks](https://github.com/Ledaryy/obsidian-todoist-completed-tasks) | `todoist-completed-tasks-plugin` | Add completed Todoist tasks to your Obsidian notes |
| [Todoist Context Bridge](https://github.com/wenlzhang/obsidian-todoist-context-bridge) | `todoist-context-bridge` | Bridge your note-taking and Todoist task management workflows with contextual connections. Seamlessly integrate with Dataview and Tasks plugins. |
| [Todoist Indicator](https://github.com/kapej42/obsidian-todoist-indicator) | `todoist-indicator` | Adds a badge to "project" files when they miss a link to a Todoist project. (based on the GTD indicator from saibotsivad, thanks!) |
| [Todoist Link](https://github.com/dennisseidel/obsidian-todoist-link) | `obsidian-todoist-link` | Create Todoist tasks and projects from Obsidian with bidirectional links. |
| [Todoist Project sync](https://github.com/stuporfly/ObsidianTodoistProjects) | `todoistprojectsync` | synchronizes projects from Todoist, creating a note for each. |
| [Todoist Review](https://github.com/imcauley/todoist-review) | `todoist-review` | A pane for reviewing overdue tasks from todoist |
| [Todoist Sync](https://github.com/jamiebrynes7/obsidian-todoist-plugin) | `todoist-sync-plugin` | Materialize Todoist tasks within Obsidian notes. |
| [Todoist Text](https://github.com/wesmoncrief/obsidian-todoist-text) | `todoist-text` | This obsidian plugin integrates your Todoist tasks with markdown checkboxes. |
| [Todos sort](https://github.com/jsifalda/obsidian-todos-sort) | `todos-sort` | Sorting your TODOs (checkboxes) in current note by completion status. |
| [TODOseq](https://github.com/scross01/obsidian-todoseq) | `todoseq` | Lightweight keyword-based task tracker using Logseq style keywords. |
| [TodoTxt](https://github.com/mvgrimes/obsidian-todotxt-plugin) | `todotxt` | Manage Todo.txt files. |
| [TodoTxt Codeblocks](https://github.com/benjamonnguyen/obsidian-todotxt-codeblocks) | `todotxt-codeblocks` | Manage your tasks inside codeblocks according to the Todo.txt specification. |
| [Toggl Track](https://github.com/mcndt/obsidian-toggl-integration) | `obsidian-toggl-integration` | Manage timers and generate time reports using Toggl Track without leaving Obsidian. |
| [Toggle Case](https://github.com/MatthewAlner/obsidian-toggle-case) | `obsidian-toggle-case` | This is an Obsidian plugin to toggle between `lowercase` `UPPERCASE` and `Title Case` |
| [Toggle Meta Yaml](https://github.com/hua03/obsidian-toggle-meta-yaml-plugin) | `obsidian-toggle-meta-yaml-plugin` | this is a simple plugin to toggle meta yaml. |
| [Toggle Readable line length](https://github.com/drichardson/obsidian-toggle-readable-line-length) | `toggle-readable-line-length` | Add command to toggle Readable line length editor setting. |
| [Toggle RTL mode](https://github.com/YoniA/toggle-rtl-obsidian-plugin) | `toggle-rtl-mode` | Toggle RTL mode using command or ribbon action |
| [ToggleList](https://github.com/thingnotok/obsidian-toggle-list) | `obsidian-toggle-list` | Toggle the list/checklist with custom states/prefixes and suffixes |
| [Tokei](https://github.com/ms3056/Tokei) | `tokei` | A simple clock. |
| [Tokenz](https://github.com/ferenk/obsidian-tokenz) | `tokenz` | Insert shortcodes into your document, e.g smileys :) or emojis :wink: . User-defined short code maps are also supported. |
| [Tolino notes Importer](https://github.com/juergenbr/obsidian-tolino-notes-import) | `tolino-notes-import` | This is a plugin for Obsidian to import notes from a Tolino E-Reader. |
| [Tomorrow's Daily Note](https://github.com/frankolson/obsidian-tomorrows-daily-note) | `obsidian-tomorrows-daily-note` | An obsidian plugin that creates tomorrow's daily note for preemtive planning. |
| [Topic Linking](https://github.com/liammagee/obsidian-topic-linking) | `obsidian-topic-linking` | Convert PDF files and web links to Markdown, and create topics from Markdown |
| [Track-a-Lot](https://github.com/revolter/obsidian-track-a-lot-plugin) | `track-a-lot` | Scrape different webpages, builds lists with the items as Markdown tables, and allows you to track their status. |
| [Tracker](https://github.com/pyrochlore/obsidian-tracker) | `obsidian-tracker` | A plugin tracks occurrences and numbers in your notes |
| [Tracker+](https://github.com/greater-than/Obsidian-Tracker-Plus) | `tracker-plus` | Track and visualize data from your notes. Compatible with original Tracker plugin. |
| [Trakt.tv Sync](https://github.com/Fleker/trakt-for-obsidian) | `trakt-tv` | Syncs your Trakt.tv shows. |
| [Transcription](https://github.com/djmango/obsidian-transcription) | `obsidian-transcription` | Transcription 3.0, now with Swiftink.io domain-aware speech-to-text! Create high-quality text transcriptions from any media file, on any device. Best-in-class ASR |
| [Transcription Audio](https://github.com/cha-yh/transcription-audio-obsidian-plugin) | `transcription-audio` | Transcribe audio files into Markdown notes. |
| [Transfer LaTeX from GPT](https://github.com/xixia123/obsidian-transfer-latex-from-gpt) | `transfer-latex-from-gpt` | This plugin allows you to transfer LaTeX equations generated by GPT into MathJax. |
| [Translate](https://github.com/Fevol/obsidian-translate) | `translate` | Translate text and notes with Google Translate, DeepL, Azure, and more. |
| [Translate Inline](https://github.com/kon-foo/Obsidian-Translate-Inline) | `translate-inline` | Translations at your fingertips. A plugin for inline Translations. |
| [Translator](https://github.com/luhaifeng666/obsidian-translator) | `obsidian-translator` | This is a plugin for Obsidian to translate selected text. |
| [Trash Explorer](https://github.com/proog/obsidian-trash-explorer) | `obsidian-trash-explorer` | Restore and delete files from the Obsidian .trash folder |
| [Tray](https://github.com/dragonwocky/obsidian-tray) | `tray` | Run Obsidian from the system tray for customisable window management & global quick notes |
| [Tree Diagram](https://github.com/limpido/obsidian-tree-diagram) | `tree-diagram` | Convert indented text to a file tree diagram. |
| [Tree Search](https://github.com/catacgc/obsidian-tree-search) | `tree-search` | The all-in-one quick switcher and bookmark manager. Zero-effort hierachical knowledge graph |
| [TreeFocus](https://github.com/iOSonntag/obsidian-plugin-treefocus) | `treefocus` | Dim, highlight & style your files & folders in the vault file explorer (foldable item navigator) based on predefined / custom rules. |
| [Trello](https://github.com/nathonius/obsidian-trello) | `obsidian-trello` | Connect an existing or new Trello card to an Obsidian note. Once connected, see basic info, add and view comments, and check off checklist items. |
| [Tressel Sync for Obsidian](https://github.com/tresselteam/obsidian-tressel) | `obsidian-tressel` | Official Tressel plugin to sync/export various content from the Internet to Obsidian |
| [Trim Whitespace](https://github.com/zlovatt/obsidian-trim-whitespace) | `obsidian-trim-whitespace` | Trims unnecessary whitespace from your Obsidian documents |
| [Truth Table+](https://github.com/Max-Schulten/truth-table-plus) | `truth-table-gen` | Generate truth tables quickly in your .md files |
| [TsumugiMark](https://github.com/mofukuru/TsumugiMark) | `tsumugi-mark` | vertical editor for Japanese writer. |
| [Tweet to Markdown](https://github.com/kbravh/obsidian-tweet-to-markdown) | `obsidian-tweet-to-markdown` | Save tweets as Markdown files, along with their images, polls, etc. |
| [Type Chinese Like English](https://github.com/Hwenyi/obsidian-type-chinese-like-english) | `type-chinese-like-english` | Convert pinyin to Chinese characters and LaTeX |
| [Typecho](https://github.com/Chen2226/obsidian-typecho) | `typecho` | Post the file to Typecho |
| [Typefully](https://github.com/dsebastien/obsidian-typefully) | `typefully` | Typefully integration. Publish social media posts with ease |
| [Typewriter Mode](https://github.com/davisriedel/obsidian-typewriter-mode) | `typewriter-mode` | Typewriter scroll, highlight current line, dim unfocused paragraphs and sentences, writing focus, restore cursor position and more. |
| [Typewriter Scroll](https://github.com/deathau/cm-typewriter-scroll-obsidian) | `cm-typewriter-scroll-obsidian` | Typewriter-style scrolling which keeps the view centered in the editor. |
| [Typing](https://github.com/konodyuk/obsidian-typing) | `typing` | Programmatic customizations for groups of notes |
| [Typing Assistant](https://github.com/Jambo2018/notion-assistant-plugin) | `typing-assistant` | Support multiple shortcut menus to improve input efficiency |
| [Typing speed](https://github.com/Supercip971/obsidian-typing-speed) | `typing-speed` | This is a plugin for showing the current typing speed in the status bar |
| [Typing Transformer](https://github.com/aptend/typing-transformer-obsidian) | `typing-transformer-obsidian` | Improved, configurable auto formatting as typing |
| [Typographer](https://github.com/coignard/obsidian-typographer) | `typographer` | Enhances typography with smart quotes, custom text replacements and auto-pairing characters. |
| [Typst Mate](https://github.com/azyarashi/obsidian-typst-mate) | `typst-mate` | Render math expressions with Typst instead of MathJax. |
| [Typst Renderer](https://github.com/fenjalien/obsidian-typst) | `typst` | Renders `typst` code blocks and math blocks with Typst. |
| [Ultimate Todoist Sync](https://github.com/HeroBlackInk/ultimate-todoist-sync-for-obsidian) | `ultimate-todoist-sync` | This is the best Todoist task synchronization plugin for Obsidian so far. |
| [umbPublisher](https://github.com/OwainWilliams/umbPublisher) | `umbpublisher` | Push notes to Umbraco CMS as content. |
| [Uncheck All](https://github.com/ShacharHarshuv/obsidian-uncheck-all) | `uncheck-all` | Uncheck all checkboxes in the current note using one command |
| [Underline](https://github.com/Benature/obsidian-underline) | `obsidian-underline` | Add underline(`<u>xxx</u>`) with shortcut, and `<center>xxx</center>`, `[[#xxx]]`, `[[#^xxx]]` |
| [Unearthed (Kindle & KOReader Sync)](https://github.com/Unearthed-App/unearthed-obsidian) | `unearthed-app` | Auto Sync Kindle/KOReader Highlights and Daily Reflection via Unearthed |
| [Unfilled Stats Highlighter](https://github.com/White7292/obsidian-hd-unfilled-stats-highlighter) | `unfilled-stats-highlighter` | The Unfilled Stats Highlighter is a practical Obsidian plugin designed to streamline your stat/habit tracking process by automatically identifying and prefixing unfilled stats, making them easier to spot and fill out. This plugin is perfect for users who frequently work with templates and require a quick and easy way to locate and complete missing information. |
| [Unicode Search](https://github.com/BambusControl/obsidian-unicode-search) | `unicode-search` | Search and insert Unicode characters into your editor |
| [unique-attachments](https://github.com/dy-sh/obsidian-unique-attachments) | `unique-attachments` |  |
| [Unit Converter](https://github.com/ruszabarov/obsidian-unit-converter) | `unit-converter` | Converts units right in your Markdown files. |
| [UNITADE.md](https://github.com/Falcion/UNITADE.md) | `unitade` | Effortlessly treat any file extension as note, organize diverse file formats in your vault and take advancements in control of extension system even with custom modals. |
| [Univer](https://github.com/dream-num/obsidian-univer) | `univer` | Create, edit, and view spreadsheets and documents in various formats like Excel and Word directly within your knowledge base. |
| [Universal renderer](https://github.com/dgudim/obsidian-universal-renderer) | `universal-renderer` | Render many different diagrams natively |
| [UnLime](https://github.com/shandyba/obsidian-lime) | `unlime` | Hide unlinked mentions in Backlinks and Outgoing Links panels |
| [Unofficial Fabric Integration](https://github.com/chasebank87/unofficial-fabric-plugin) | `unofficial-fabric-integration` | Integrates Fabric into your vault |
| [Unofficial Supernote by Ratta Integration](https://github.com/philips/supernote-obsidian-plugin) | `supernote` | View Supernote notes, generate markdown from note and capture screen mirror. |
| [Upcoming](https://github.com/charliecm/obsidian-upcoming) | `obsidian-upcoming` | Open upcoming and/or past daily notes in their own panes, tabs, or windows. |
| [Update modified date](https://github.com/alangrainger/obsidian-frontmatter-modified-date) | `frontmatter-modified-date` | Automatically update a frontmatter modified date field when you modify your note. This will not use the filesystem time, but only when you modify the file through Obsidian. Optionally store a history of edit times. |
| [Update Relative Links](https://github.com/val3344/obsidian-update-relative-links) | `update-relative-links` | Update relative links. |
| [Update Time](https://github.com/dsebastien/obsidian-update-time) | `update-time` | Automatically update front matter to include creation and last update times. |
| [Update time on edit](https://github.com/beaussan/update-time-on-edit-obsidian) | `update-time-on-edit` | Keep front matter in sync with the last edit time |
| [Update Time Updater](https://github.com/muratagawa/update-time-updater) | `update-time-updater` | Update the 'update time' element when saving or manually. |
| [URI Commands](https://github.com/kzhovn/uri-commands-obsidian) | `uri-commands` | Execute URIs from the Obsidian command palette. |
| [URI Converter](https://github.com/wenlzhang/obsidian-uri-converter) | `uri-converter` | Convert URIs to internal links. |
| [URL Display](https://github.com/lin-stephanie/obsidian-url-display) | `url-display` | Extract and display external URLs of the note in Obsidian. |
| [URL Formatter](https://github.com/thomassnoeck/url-formatter-obsidian) | `url-formatter` | Automatically formats specific URLs pasted into your notes into clean Markdown links. |
| [URL Namer](https://github.com/zfei/obsidian-url-namer) | `url-namer` | This plugin retrieves the HTML titles to name the raw URL links. |
| [User Plugins](https://github.com/mnowotnik/obsidian-user-plugins) | `obsidian-user-plugins` | Use ts and js modules or js snippets to code your own plugins |
| [UseSemaLogic](https://github.com/MM-GO/UseSemaLogic) | `semalogic` | Real-time use of the SemaLogic formal language |
| [Usher](https://github.com/vrtmrz/usher) | `usher` | The overridden config directory manager |
| [Vantage - Advanced search builder](https://github.com/ryanjamurphy/vantage-obsidian) | `vantage-obsidian` | Build advanced search queries in Obsidian. |
| [VARE](https://github.com/4Source/vare-obsidian-plugin) | `vare` | Now you can easily manage your plugins and themes. Simply select the version you want or install unlisted versions from GitHub. You can also install beta version and switch back if necessary. |
| [Variant Editor](https://github.com/kunalJa/VariantEditor) | `variant-editor` | Create variations of words and sentences and compare them, in context, with a single click |
| [Varinote](https://github.com/gsarig/obsidian-varinote) | `varinote` | Add variables in templates and set their values on-the-fly during the note creation. |
| [Various Complements](https://github.com/tadashi-aikawa/obsidian-various-complements-plugin) | `various-complements` | This plugin enables you to complete words like the auto-completion of IDE |
| [Vault 2 Book](https://github.com/Mitra98t/vault2book-plugin) | `vault-2-book` | Converts your notes to a book creating a single file containing all the notes linked |
| [Vault Changelog](https://github.com/philoserf/obsidian-vault-changelog) | `obsidian-vault-changelog` | Maintain a changelog of recently edited notes |
| [Vault Chat](https://github.com/exoascension/vault-chat) | `vault-chat` | A ChatGPT bot trained on your vault notes. Ask your AI questions about your own thoughts and ideas! |
| [Vault Encrypt](https://github.com/Pluppen/obsidian-vault-encrypt-plugin) | `vault-encrypt` | Encrypts and decrypts the contents of the vault using a password. |
| [Vault Explorer](https://github.com/decaf-dev/obsidian-vault-explorer) | `vault-explorer` | Explore your vault in visual format |
| [Vault File Renamer](https://github.com/louanfontenele/obsidian-vault-file-renamer) | `vault-file-renamer` | Standardizes names in your vault: lowercase, accents removed, spaces become hyphens, and invalid characters are converted. Settings include enable/disable, target extensions (allow-list), excluded extensions (when allow-list is empty), and folder blacklist. |
| [Vault Full Statistics](https://github.com/jtprogru/obsidian-vault-full-statistics-plugin) | `vault-full-statistics` | Status bar item with vault full statistics such as number of notes, files, attachments, links, tags and quality of vault. |
| [Vault LLM Assistant](https://github.com/brianstm/obsidian-vault-llm-assistant) | `vault-llm-assistant` | Uses AI to answer questions and create notes about your vault with proper citations |
| [Vault Name](https://github.com/gapmiss/obsidian-vault-name) | `vault-name` | Display and customize the vault name (title) in the side navigation file explorer. |
| [Vault Nickname](https://github.com/rscopic/obsidian-vault-nickname) | `vault-nickname` | Override the vault's display name and/or title order. Intended to disambiguate vaults with the same folder name when adhering to a common folder structure between projects. |
| [Vault Review](https://github.com/SashaKryzh/obsidian-vault-review) | `vault-review` | Randomly review your vault and track progress. |
| [Vault Size History](https://github.com/technerium/obsidian-vault-size-history) | `vault-size-history` | Graph of the number of files in the Vault. |
| [Vault Statistics](https://github.com/bkyle/obsidian-vault-statistics-plugin) | `obsidian-vault-statistics-plugin` | Status bar item with vault statistics such as number of notes, files, attachments, and links. |
| [Vault Stats](https://github.com/blueheron786/obsidian-stats-plugin) | `vault-stats` | Provides methods to retrieve statistics about the vault, such as the number of notes, total word count, recently modified notes, and more. |
| [Vault to blog](https://github.com/barkstone2/vault-to-blog) | `vault-to-blog` | Publish the vault to a GitHub Pages blog. |
| [Vault Transfer](https://github.com/ImaginaryProgramming/obsidian-vault-transfer) | `vault-transfer` | Copies a note, and pastes it into another vault. |
| [VaultAI](https://github.com/0xneobyte/VaultAI) | `vault-ai` | Transform your note-taking with an intelligent AI assistant powered by Google's Gemini AI. Features a sleek floating chat interface for seamless writing assistance, content generation, and smart note enhancement. |
| [VaultSync](https://github.com/thewordisbird/VaultSync) | `vault-sync` | Sync vault with cloud storage provider. |
| [VCF Contacts](https://github.com/broekema41/obsidian-vcf-contacts) | `vcf-contacts` | Effortlessly manage, organize, and interact with your contacts. Import, export, and structure vCard (VCF) files seamlessly while keeping all contact details accessible in your knowledge base. Includes click-to-call, right-click copy, structured metadata, and more! |
| [vConsole](https://github.com/zhouhua/obsidian-vconsole) | `vconsole` | Integrate vConsole for developers to facilitate the debugging of mobile plugins. |
| [Vector Search](https://github.com/ashwin271/obsidian-vector-search) | `vector-search` | Semantic search for your notes using Ollama and nomic-embed-text embeddings. Requires Ollama installation. |
| [Vega Visualizations](https://github.com/Justin-J-K/obsidian-vega) | `obsidian-vega` | Create highly-customizable data visualizations like line charts and scatter plots using Vega or Vega-Lite. |
| [Verovio Music Renderer](https://github.com/kpaede/Verovio-Music-Renderer) | `verovio-music-renderer` | Rendering, playback and export of MEI, MusicXML, ABC and PAE music notation files and embeds. |
| [Verse of the Day](https://github.com/janisringli/verse-of-the-day-for-obsidian) | `verse-of-the-day` | Lets you add the verse of the day from YouVersion to your daily notes |
| [Version Control](https://github.com/Yuichi-Aragi/Version-Control) | `version-control` | Create intentional snapshots with meaningful names, in-file branching, side-by-side diffs, timeline search, writing stats, and optional auto-saves. |
| [Version History Diff](https://github.com/kometenstaub/obsidian-version-history-diff) | `obsidian-version-history-diff` | Diff the version history of the core Sync and File Recovery plugins and Git. |
| [Vertical Tabs](https://github.com/oxdc/obsidian-vertical-tabs) | `vertical-tabs` | Offer an alternative view that displays open tabs vertically, allowing users to group and organize tabs for a better navigation experience. |
| [Vertical Timeline List](https://github.com/Jalad25/vertical-timeline-list) | `vertical-timeline-list` | Utilizes task lists to create a timeline... or something resembling a timeline. |
| [Vextab](https://github.com/luigman/obsidian-vextab) | `vextab` | An Obsidian plugin for rendering guitar tablature and music notation using Vextab. |
| [View Count](https://github.com/decaf-dev/obsidian-view-count) | `view-count` | Track view count for each vault file. |
| [Viewer ftags](https://github.com/d7sd6u/obsidian-viewer-ftags) | `viewer-ftags` | Add file's ftags as chips at the top of the markdown view. |
| [Vikunja Sync](https://github.com/Heiss/obsidian-vikunja-plugin) | `vikunja-sync` | Integrates Vikunja. |
| [Vim IM Control](https://github.com/hideakitai/obsidian-vim-im-control) | `vim-im-control` | Control Input Method (IM) when `InsertLeave` and `InsertEnter` in Vim mode. Supports macOS, Windows, and Linux. |
| [Vim IM Select](https://github.com/ALONELUR/vim-im-select-obsidian) | `vim-im-select` | Support auto select the apposite input method in different vim mode |
| [Vim Marker Sharpener](https://github.com/artemDvoryadkin/obsidian-vim-marker-sharpener) | `vim-marker-sharpener` | Text formatting commands in Vim mode. Supports applying styles (bold, italic, etc.). Works correctly in visual mode with selected text. |
| [Vim Multibyte Char Search](https://github.com/anselmwang/obsidian-vim-multibyte-char-search) | `obsidian-vim-multibyte-char-search` | Search multibyte characters by the first character of corresponding ASCII encoding of input method. For example, for Chinese, search by the first character of Pinyin. |
| [Vim Toggle](https://github.com/connerohnesorge/vim-toggle) | `vim-toggle` | A plugin for Obsidian that enables the toggling vim mode to on and off inside of the editor. |
| [Vim Yank Highlight](https://github.com/aleksey-rowan/obsidian-vim-yank-highlight) | `vim-yank-highlight` | Highlight yanked text in Vim mode. Enjoy that subtle animation you've missed so much. |
| [Vimium](https://github.com/karstenpedersen/obsidian-vimium) | `vimium` | Interact with elements using keyboard shortcuts in the spirit of Vim |
| [Vimrc Support](https://github.com/esm7/obsidian-vimrc-support) | `obsidian-vimrc-support` | Auto-load a startup file with Obsidian Vim commands. |
| [VirtFolder](https://github.com/gr0grig/obsidian-virt-folder) | `virt-folder` | Creating a hierarchical structure like Luhmann's Zettelkasten |
| [Virtual Content](https://github.com/Signynt/virtual-content) | `virtual-footer` | Display markdown text (including dataview queries or Obsidian bases) at the bottom, top or in the sidebar for all notes which match a specified rule, without modifying them. |
| [Virtual Linker / Glossary](https://github.com/vschroeter/obsidian-virtual-linker) | `virtual-linker` | Automatically creates virtual links for text within your notes that match the titles or aliases of other notes in your vault. Create a glossary-like functionality, show unlinked mentions and transform them to real links. |
| [Virus Total Enrichment](https://github.com/ytisf/virustotal-enrich) | `virustotal-enrich` | Enrich your notes with information from VirusTotal. |
| [Vision Recall](https://github.com/travisvn/obsidian-vision-recall) | `vision-recall` | Transform screenshots into searchable notes using AI vision and text analysis. |
| [Visited Countries](https://github.com/IvanPeshykov/obsidian-visited-countries) | `visited-countries` | The interactive map where you can select countries that you've visited. |
| [Visual Crossing Weather](https://github.com/willasm/vc-weather) | `visual-crossing-weather` | Visual Crossing Weather API for Your Notes |
| [Vitepress Publisher](https://github.com/tyrad/obsidian-vitepress) | `vitepress-publisher` | This is a plugin for more convenient preview and publishing of .md files using VitePress and other static site generators like Hugo |
| [Vk group notifier](https://github.com/filichev-evgeny/obsidianvkupdatenotifier) | `vk-group-notifier` | Track news posts from the vk.com groups. |
| [VLC Bridge](https://github.com/zuluwi/obsidian-vlc-bridge) | `vlc-bridge` | Take video/movie notes with timestamp links and snapshots from VLC Player. |
| [Vocabulary Cards](https://github.com/meniam/obsidian-vocabulary-cards) | `vocabulary-cards` | An easy way to display vocabulary words as flashcards and as a list. |
| [Vocabulary Highlighter](https://github.com/eatgrass/obsidian-vocab-highlighter) | `vocabulary-highlighter` | Hightlight vocabulary based on the word frequency |
| [Vocabulary View](https://github.com/nnshi-s/obsidian-vocabulary-view-plugin) | `obsidian-vocabulary-view` | Write down some words with their explanations and preview them in a vocabulary test style |
| [Voice](https://github.com/chrisurf/obsidian-voice) | `voice` | Text-to-speech adds sound, audio, and speech to your notes, letting them talk in your workspace, mobile-friendly, perfect for learning or reinforcing ideas as you listen hands-free in an audiobook-like experience. |
| [Voicenotes Sync](https://github.com/voicenotes-community/voicenotes-sync) | `voicenotes-sync` | Synchronize your notes from Voicenotes.com |
| [Vox](https://github.com/vincentbavitz/obsidian-vox) | `vox` | Intelligently trancribe and categorize your voice notes |
| [VSCode Editor](https://github.com/sunxvming/obsidian-vscode-editor) | `vscode-editor` | Edit Code Files like VSCode. |
| [Waka time box](https://github.com/simonla/obsidian_waka_box) | `waka_time_box` | Show daily coding activity from WakaTime |
| [WakaTime](https://github.com/wakatime/obsidian-wakatime) | `obsidian-wakatime` | Automatic time tracking and metrics generated from your Obsidian usage activity. |
| [Wakatime / Wakapi](https://github.com/Kovah/obsidian-wakatime) | `wakatime-kvh` | Connect to Wakatime or Wakapi to track the time spent while browsing or writing notes. |
| [Wardley Maps](https://github.com/damonsk/obsidian-wardley-maps) | `wardley-maps` | View and edit Wardley Maps using the Online Wardley Maps format. |
| [Watched-Metadata](https://github.com/NailAhmed/Watched-Metadata) | `watched-metadata` | Watches for changes in metadata and performs user-specified actions based on these changes. |
| [Water Tracker](https://github.com/LuigiCerone/obsidian-water-tracker) | `water-tracker` | Keep track of how much water you drunk |
| [WaveDrom](https://github.com/kingsquirrel152/obsidian-wavedrom) | `obsidian-wavedrom` | This is very rough and quick integration of WaveDrom into obsidian |
| [Waveform Player](https://github.com/zhouhua/obsidian-waveform-player) | `waveform-player` | Render audio files as waveforms |
| [Wayback Archiver](https://github.com/IshizuEitaro/obsidian-wayback-archiver) | `wayback-archiver` | Automatically archives web links via Wayback Machine and appends archived versions in notes. |
| [Waypoint](https://github.com/IdreesInc/Waypoint) | `waypoint` | Easily generate dynamic content maps in your folder notes using waypoints. Enables folders to show up in the graph view and removes the need for messy tags! |
| [Weather Widget](https://github.com/mr-asa/obsidian_weather) | `weather-widget` | Weather widget for display in notes, Canvas, and a separate tab. |
| [Web viewer Bookmarks](https://github.com/stefandanzl/webviewer-bookmarks) | `webviewer-bookmarks` | Create and manage bookmarks for the built-in Web viewer. |
| [WebDAV Explorer](https://github.com/sunmagicshow/obsidian-webdav) | `webdav-explorer` | WebDAV Explorer: Connect to WebDAV server, preview files directly in web view, and generate links through simple drag-and-drop. |
| [Webdav File Explorer](https://github.com/red0orange/obsidian-webdav-file-explorer) | `webdav-file-explorer` | A webdav file explorer for Obsidian. |
| [WebDAV Image Uploader](https://github.com/Koishiiko/obsidian-webdav-image-uploader) | `webdav-image-uploader` | Uploads, downloads and deletes images on WebDAV server within notes. |
| [Webhook Plugin](https://github.com/trashhalo/obsidian-webhooks) | `obsidian-webhooks` | Plugin that connects your notes to the internet of things through webhooks! |
| [Webpage HTML Export](https://github.com/KosmosisDire/obsidian-webpage-export) | `webpage-html-export` | Export html from single files, canvas pages, or whole vaults. Direct access to the exported HTML files allows you to publish your digital garden anywhere. Focuses on flexibility, features, and style parity. |
| [Wechat Public Platform](https://github.com/ai-chen2050/obsidian-wechat-public-platform) | `wechat-public-platform` | Release the article from your vault to WeChat, Baidu Baijiahao, or another article release platform. |
| [Week Planner](https://github.com/rwirdemann/obsidian-week-planner) | `obsidian-week-planner` | Week Planner plugin for Obsidian. This plugin defines commands for creating planning documents and moving tasks between them. |
| [Weekly Goal Tracker](https://github.com/GitGorman/weekly-goal-tracker) | `weekly-goal-tracker` | Keep track of weekly/daily goals in the status bar |
| [Weekly Review](https://github.com/brandonkboswell/weekly-review) | `weekly-review` | This opens all of the files you have created in the last week to support easy Weekly Reviews. |
| [Weekly Review notes linker](https://github.com/AdityaKhowalGithub/weekly-review-notes-linker) | `weekly-review-linker` | This links all of the files you have created in the last week into a Weekly Review note. |
| [Weread](https://github.com/zhaohongxuan/obsidian-weread-plugin) | `obsidian-weread-plugin` | This is obsidian plugin for Tencent weread. |
| [WeWrite](https://github.com/learnerchen-forever/wewrite) | `wewrite` | Make obsidian a powerful workspace for writing and publishing article to WeChat MP. Draft ahead  of release. |
| [WhatsApp backup importer](https://github.com/LuigiCerone/obsidian-whatsapp-backup-importer) | `whatsapp-backup` | Import WhatsApp export inside a note |
| [WhatsApp export note](https://github.com/JoaoEmanuell/obsidian-whatsapp-export-note) | `whatsapp-export-note` | Convert the current note for WhatsApp format to share. |
| [Wheel Tab Switcher](https://github.com/22-2/wheel-tab-switcher) | `wheel-tab-switcher` | Switch between Tabs using your mouse wheel when hovering over tab headers |
| [Whisper](https://github.com/nikdanilov/whisper-obsidian-plugin) | `whisper` | Speech-to-text in Obsidian using OpenAI Whisper |
| [WHISPERER.md](https://github.com/Falcion/Whisperer.md) | `whisperer` | Play ambience in your vault, assign audio to files through metadata with support of local (from vault) and URLs (Youtube, Soundcloud) versions of audio: works on mobile vaults. |
| [White Noise](https://github.com/zhouhua/obsidian-white-noise) | `white-noise` | Play white noise to help you focus on your work |
| [Widgets](https://github.com/rafaelveiga/obsidian-widgets) | `widgets` | Add widgets to your notes like clock, countdown, and quotes. |
| [Wielder](https://github.com/victorb/obsidian-wielder) | `wielder` | Clojure inside Obsidian |
| [Wikidata Importer](https://github.com/samwho/obsidian-wikidata-importer) | `wikidata-importer` | Import data from Wikidata into your vault. |
| [WikiDocs](https://github.com/pahkey/obsidian-wikidocs-plugin) | `wikidocs` | Fetch, edit, and upload WikiDocs books. |
| [Wikilinks to MDLinks](https://github.com/agathauy/wikilinks-to-mdlinks-obsidian) | `wikilinks-to-mdlinks-obsidian` | A plugin that converts wikilinks to markdown links and vice versa |
| [Wikipedia](https://github.com/jmilldotdev/obsidian-wikipedia) | `obsidian-wikipedia` | Grabs information from Wikipedia for a topic and brings it into Obsidian notes |
| [Wikipedia Helper](https://github.com/StrangeGirlMurph/obsidian-wikipedia-helper) | `wikipedia-search` | Search, link, insert and open Wikipedia/Wikimedia articles. |
| [WonderBox](https://github.com/Chrstn67/WonderBox) | `wonderbox` | Create more relevant text sections your tips, top notes, warnings and more. |
| [Word Frequency](https://github.com/mts7/obsidian-word-frequency) | `word-frequency` | Counts the most frequently used words in a note and displays them in the sidebar. |
| [Word Splitting for Japanese in Edit Mode](https://github.com/sonarAIT/cm-japanese-patch) | `japanese-word-splitter` | A patch for Obsidian's built-in CodeMirror Editor to support Japanese word splitting |
| [Word Splitting for Simplified Chinese in Edit Mode and Vim Mode](https://github.com/aidenlx/cm-chs-patch) | `cm-chs-patch` | A patch for Obsidian's built-in CodeMirror Editor to support Simplified Chinese word splitting |
| [Word Sprint](https://github.com/kinabalu/obsidian-word-sprint) | `obsidian-word-sprint` | Word Sprint for Obsidian plugin for your writing projects like Nanowrimo |
| [WordCraft](https://github.com/danferns/obsidian-wordcraft) | `wordcraft` | Find rhymes, synonyms, and describing words. Designed for songwriting and poetry. |
| [Wordflow Tracker](https://github.com/LeCheenaX/WordFlow-Tracker) | `wordflow-tracker` | Track the changes and stats of your edited note files automatically. Record the modified notes and statistics to your daily note with various customizations! |
| [WordNet Dictionary](https://github.com/TfTHacker/Obsidian-WordNet) | `obsidian-wordnet-plugin` | WordNet is a large lexical database of English developed by Princeton University. |
| [Wordnik Definitions](https://github.com/lizard-heart/obsidian-wordnik-definitions) | `obsidian-wordnik` | Grabs information from Wordnik for a topic and brings it into Obsidian notes |
| [WordPress](https://github.com/devbean/obsidian-wordpress) | `obsidian-wordpress` | A plugin for publishing Obsidian documents to WordPress. |
| [WordWise](https://github.com/ckt1031/obsidian-wordwise-plugin) | `wordwise` | Writing companion for AI content generation. |
| [Wordy](https://github.com/nqthqn/obsidian-wordy) | `obsidian-wordy` | Thesaurus, rhymes, alliterations, dictionary and more using the Datamuse API |
| [Workbench](https://github.com/ryanjamurphy/workbench-obsidian) | `workbench-obsidian` | Keep a workbench of knowledge materials. |
| [Workbooks](https://github.com/Canna71/obsidian-sheets) | `workbooks` | Work with Spreadsheets inside your notes |
| [Workona Import](https://github.com/Holmes555/workona-to-obsidian) | `workona-to-obsidian` | Import Workona resources, tabs, notes and tasks through generated JSON file. |
| [Workout Planner](https://github.com/SpatariuRares/obsidian-workout-plugin) | `workout-planner` | Visualize workout data with interactive charts and advanced search capabilities. |
| [Workout Tracker](https://github.com/wanabeunique/obsidian-workout-tracker) | `workout-tracker` | Log workouts, track progress, and view exercise statistic. |
| [Workspaces Plus](https://github.com/jsmorabito/obsidian-workspaces-plus) | `workspaces-plus` | Quickly switch and manage workspaces |
| [Wrap with shortcuts](https://github.com/manic/obsidian-wrap-with-shortcuts) | `obsidian-wrap-with-shortcuts` | Wrap selected text in custom tags with shortcuts. E.g.: underline, sub, ruby(フリガナ) |
| [Write Good](https://github.com/markahesketh/write-good-obsidian) | `write-good` | Linter for English prose and improving writing style |
| [Writeas Blog Publisher](https://github.com/encima/obsidian-writeas-plugin) | `writeas-publisher` | Publish your notes to write.as |
| [Writing](https://github.com/johackim/obsidian-writing) | `writing` | Write and format your next book directly from Obsidian |
| [Writing Goals](https://github.com/lynchjames/obsidian-writing-goals) | `writing-goals` | Set dynamic writing goals for notes and folders in Obsidian. |
| [WuCai highlights Official](https://github.com/makediff/obsidian-wucai) | `wucai-highlights-official` | Official WuCai highlights <-> Obsidian integration |
| [Wypst](https://github.com/andredalbosco/obsidian-wypst) | `wypst` | Typst math typesetting for Obsidian. |
| [X Post Saver](https://github.com/tanaka-mambinge/x-post-saver) | `x-post-saver` | Saves X (formerly Twitter) posts' text data to new notes or inside a specific directory in your vault. |
| [x86 Assembly Flow Graphing](https://github.com/dwolfe884/obsidian-x86-flow-graph) | `x86-flow-graphing` | An Obsidian plugin for converting x86 code blocks into flow graphs |
| [Xiaohongshu Importer](https://github.com/bnchiang96/xiaohongshu-importer) | `xiaohongshu-importer` | Import Xiaohongshu (小红书) notes with media and categorization. |
| [XMind Linker](https://github.com/leafney/obsidian-xmind-linker) | `xmind-linker` | View XMind files in your vault and connect to XMind software for editing. |
| [XMind Viewer](https://github.com/Ssentiago/obsidian-xmind-viewer) | `xmind-viewer` | Integrate viewing of your XMind files |
| [Xournal++](https://github.com/jonjampen/obsidian-xournalpp) | `xournalpp` | Integration with Xournal++ for handwritten notes and annotations. |
| [Yaml Manager](https://github.com/lijyze/obsidian-state-switcher) | `obsidian-state-switcher` | Keep you away from directly operating of yaml front matter |
| [YAML Table](https://github.com/dainakai/obsidian-yaml-table) | `yaml-table` | Transform YAML code blocks into HTML tables for better visualization |
| [Yandex Tracker Issue](https://github.com/CubieProg/Obsidian-Yandex-Tracker-Issue) | `yandex-tracker-issue` | Display Yandex Tracker issues in your notes |
| [Yandex Wiki Integration](https://github.com/CubieProg/Obsidian-Yandex-Wiki-Integration) | `yandex-wiki-integration` | Integration with Yandex Wiki knowledge base |
| [Yanki](https://github.com/kitschpatrol/yanki-obsidian) | `yanki` | Sync flashcards from a folder in your vault to Anki. Pure Markdown syntax. No fuss. |
| [Yearly Diary Comparator](https://github.com/kiitosu/yearly-diary-comparator) | `yearly-diary-comparator` | Show a side-by-side yearly comparison of diary in daily notes |
| [Yearly Glance](https://github.com/Moyf/yearly-glance) | `yearly-glance` | Year at a glance - overview of annual events with customizable management options. |
| [Yesterday](https://github.com/dominikmayer/obsidian-yesterday) | `yesterday` | Transform your notes into a visually stunning diary, integrating dialogs, chat logs, and media content blocks for a seamless journaling experience. |
| [Yesterday's note](https://github.com/trevortylerlee/yesterdays-note) | `yesterdays-note` | Open yesterday's daily note. |
| [YOLO](https://github.com/Lapis0x0/obsidian-yolo) | `yolo` | Agent-native AI assistant — chat, write, search, orchestrate, all in one. |
| [You and Your Research](https://github.com/neozhang/you-and-your-research) | `you-and-your-research` | Research with the help of A.I. |
| [Youglish Plugin](https://github.com/nhaouari/obsidian-youglish-plugin) | `obsidian-youglish-plugin` | Use YouTube to improve your pronunciation. YouGlish gives you fast, unbiased answers about how words is spoken by real people and in context. |
| [YouHaveBeenStaring](https://github.com/fxal/obsidian-youhavebeenstaring-plugin) | `youhavebeenstaring-plugin` | This plugin tells you in the status bar for how long you've been staring at your obsidian vault. Well - at least how long your vault is open. |
| [YourPulse - Your Writing Activity Visualised](https://github.com/jsifalda/obsipulse-plugin) | `yourpulse` | It's like your Github profile, but for your vault (featuring daily streak, average daily word count, comprehensive stats and plugins overview). |
| [YouTrack Fetcher](https://github.com/forketyfork/obsidian-youtrack-fetcher) | `youtrack-fetcher` | Fetches YouTrack issues into notes. |
| [YouTube downloader](https://github.com/ai-chen2050/obsidian-youtube-downloader) | `youtube-downloader` | Download video from YouTube |
| [Youtube Iframe Timestamps](https://github.com/NilsLeo/obsidian-youtube-iframe-timestamps) | `youtube-iframe-timestamps` | Allows you to embed YouTube videos with timestamps directly in your notes, enabling seamless referencing and note-taking without needing to open a separate browser window. |
| [Youtube Summarizer](https://github.com/ozdemir08/youtube-video-summarizer) | `youtube-summarizer` | A plugin to summarize the transcripts of Youtube videos. |
| [YouTube Template](https://github.com/sundevista/youtube-template) | `youtube-template` | A plugin that would help you to fetch YouTube videos data into your vault. |
| [YouTube Video Summarizer](https://github.com/mbramani/obsidian-yt-video-summarizer) | `yt-video-summarizer` | Summarize YouTube videos using Gemini AI. Extract transcripts, generate summaries, and create structured notes. |
| [YouVersion Linker](https://github.com/jaanonim/obsidian-youversion-linker) | `youversion-linker` | Automatically link bible verses in your notes to YouVersion bible. |
| [YTranscript](https://github.com/lstrzepek/obsidian-yt-transcript) | `ytranscript` | This is simple plugin to fetch transcription for Youtube. |
| [YTSummarizer](https://github.com/ardakalayci/ytsummarizer) | `yt-summarizer` | Fetches YouTube transcripts and generates summaries using OpenAI GPT models |
| [Yuque Publish](https://github.com/oylbin/obsidian-yuque-publish) | `yuque-publish` | Publish your notes to Yuque. |
| [Zen](https://github.com/Maxymillion/zen) | `zen` | A focus mode Obsidian plugin. |
| [Zen Mode](https://github.com/paperbenni/obsidian-zenmode) | `zenmode` | Hide most UI elements |
| [Zen Space](https://github.com/amatya-aditya/obsidian-zen-space) | `zen-space` | A focused file explorer for Obsidian showing only the files in the current folder. |
| [ZettelFlow](https://github.com/RafaelGB/Obsidian-ZettelFlow) | `zettelflow` | Helps you to create and manage your notes in a Zettelkasten way via Canvas. |
| [ZettelGPT](https://github.com/OverRaddit/ZettelGPT) | `zettelgpt` | ZettelGPT: Turbocharge Your Note-taking with AI Assistance |
| [Zettelkasten Branch Tracker](https://github.com/thelivingphilosophy/zettelkasten-branch-tracker) | `zettelkasten-branch-tracker` | Track and visualize the branching structure of your Zettelkasten notes |
| [Zettelkasten LLM Tools](https://github.com/glovguy/obsidian-gpt-zettelkasten) | `zettelkasten-llm-tools` | Zettelkasten note taking powered by AI |
| [zettelkasten navigation](https://github.com/PKM-er/obsidian-zettelkasten-navigation) | `zettelkasten-navigation` | Visualize a Luhmann-style zettelkasten. |
| [Zettelkasten Outliner](https://github.com/tylersuzukinelson/zettelkasten-outliner) | `zettelkasten-outliner` | Provides a list representation for your Zettelkasten. |
| [Zhihu](https://github.com/zimya/zhihu_obsidian) | `zhihu` | Enable you to publish your articles and answers to Zhihu |
| [Zhongwen Block](https://github.com/0918nobita/obsidian-zhongwen-block) | `zhongwen-block` | Provides code blocks with features for Chinese learners |
| [Zhongwen Reader](https://github.com/natipt/obsidian-zhongwen-reader) | `zhongwen-reader` | Chinese-English hover dictionary and vocabulary management plugin. |
| [Zoom](https://github.com/vslinko/obsidian-zoom) | `obsidian-zoom` | Zoom into heading and lists. |
| [Zoottelkeeper Plugin](https://github.com/akosbalasko/zoottelkeeper-obsidian-plugin) | `zoottelkeeper-obsidian-plugin` | This plugin automatically creates, maintains and tags MOCs for all your folders. |
| [Zotero Bridge](https://github.com/vanakat/zotero-bridge) | `zotero-bridge` | Zotero integration |
| [Zotero Integration](https://github.com/obsidian-community/obsidian-zotero-integration) | `obsidian-zotero-desktop-connector` | Insert and import citations, bibliographies, notes, and PDF annotations from Zotero. |
| [Zotero Link](https://github.com/vanakat/zotero-link) | `zotero-link` | Insert link to Zotero items from Obsidian interface using Zotero Bridge |
| [Zotero Sync](https://github.com/frthjf/obsidian-zotero-sync-client) | `zotero-sync-client` | Zotero API client to sync your Zotero library into your vault |
| [ZotLit](https://github.com/PKM-er/obsidian-zotlit) | `zotlit` | Plugin to integrate with Zotero, create literature notes and insert citations from a Zotero library. |
| [复制图文 (Copy Image Text)](https://github.com/msgk239/obsidian-copy-image-text) | `copy-image-text` | Copy note content (including text and images) to clipboard. 复制笔记内容（包括文本和图片）到剪贴板。 |
| [新枝Newledge](https://github.com/DepartingAgain/obsidian-newledge) | `newledge` | Import Newledge data. |
| [盘古 PanGu](https://github.com/Natumsol/obsidian-pangu) | `obsidian-pangu` | 自动为中英文之间插入空格，排版强迫者的福音。 |

---

## Themes (416)

| Name | Package ID | Description |
|------|-----------|-------------|
| [80's Neon](https://github.com/deathau/80s-Neon-for-Obsidian.md) | `80s-neon` |  |
| [Abate](https://github.com/ricedev10/Abate-theme) | `abate` |  |
| [Abecedarium](https://github.com/zalenza/Abecedarium-theme) | `abecedarium` |  |
| [absolutegruv](https://github.com/kkYrusobad/AbsoluteGruv) | `absolutegruv` |  |
| [Abyssal](https://github.com/tazpellegrini/abyssalobsidian) | `abyssal` |  |
| [Adrenaline](https://github.com/Spekulucius/obsidian-adrenaline) | `adrenaline` |  |
| [Adwaita](https://github.com/birneee/obsidian-adwaita-theme) | `adwaita` |  |
| [Agate](https://github.com/solm0/Agate) | `agate` |  |
| [aged whisky](https://github.com/incantatem2/Obsidian-aged-whisky) | `aged-whisky` |  |
| [al-dente](https://github.com/chad-bennett/al-dente-obsidian-theme) | `al-dente` |  |
| [Allium](https://github.com/xainapse/Allium) | `allium` |  |
| [amethyst](https://github.com/cotemaxime/obsidian-amethyst) | `amethyst` |  |
| [AMOLED Serenity](https://github.com/darthdemono/AMOLED-Serenity) | `amoled-serenity` |  |
| [Antique Flowers](https://github.com/incantatem2/Obsidian-antique-flowers) | `antique-flowers` |  |
| [AnuPpuccin](https://github.com/AnubisNekhet/AnuPpuccin) | `anuppuccin` |  |
| [Apatheia](https://github.com/AmadeusWM/Obsidian-Apatheia) | `apatheia` |  |
| [Apex](https://github.com/clearlysid/apex) | `apex` |  |
| [Arcane](https://github.com/xRyul/obsidian-arcane-theme) | `arcane` |  |
| [ars-magna](https://github.com/mediapathic/obsidian-arsmagna-theme) | `ars-magna` |  |
| [Arzaba](https://github.com/DarioArzaba/Obsidian-Theme-Arzaba) | `arzaba` |  |
| [atom](https://github.com/kognise/obsidian-atom) | `atom` |  |
| [Auger](https://github.com/davidgolding/obsidian-auger) | `auger` |  |
| [Aura](https://github.com/shadowash8/obsidian-aura) | `aura` |  |
| [Aura Dark](https://github.com/possibly-not/obsidian-aura-theme) | `aura-dark` |  |
| [aurora](https://github.com/auroral-ui/aurora-obsidian-md) | `aurora` |  |
| [Aurora-Twilight](https://github.com/Quinta0/Aurora-Twilight) | `aurora-twilight` |  |
| [Autotape](https://github.com/1612elphi/autotape-theme) | `autotape` |  |
| [Avatar](https://github.com/cxj05h/obsidian-avatar) | `avatar` |  |
| [ayu](https://github.com/bcdavasconcelos/Obsidian-Ayu) | `ayu` |  |
| [ayu-mirage](https://github.com/bcdavasconcelos/Obsidian-Ayu_Mirage) | `ayu-mirage` |  |
| [Azure](https://github.com/annagracedev/obsidian-azure) | `azure` |  |
| [Base16 Default Dark](https://github.com/flowing-abyss/obsidian-base16-default-dark) | `base16-default-dark` |  |
| [base2tone](https://github.com/deathau/Base2Tone-For-Obsidian.md) | `base2tone` |  |
| [Baseline](https://github.com/aaaaalexis/obsidian-baseline) | `baseline` |  |
| [Behave dark](https://github.com/Chrismettal/Obsidian-Behave-dark) | `behave-dark` |  |
| [Black](https://github.com/b3h3m0th/black-obsidian-theme) | `black` |  |
| [blackbird](https://github.com/vanadium23/obsidian-blackbird-theme) | `blackbird` |  |
| [Blood Rush](https://github.com/incantatem2/Obsidian-blood-rush) | `blood-rush` |  |
| [Blossom](https://github.com/BlossomTheme/Obsidian) | `blossom` |  |
| [blue-topaz](https://github.com/PKM-er/Blue-Topaz_Obsidian-css) | `blue-topaz` |  |
| [Blur](https://github.com/Jawuj/Blur-Theme) | `blur` |  |
| [Bolt](https://github.com/Bluemoondragon07/Obsidian-Bolt) | `bolt` |  |
| [Border](https://github.com/Akifyss/obsidian-border) | `border` |  |
| [Borealis](https://github.com/juanchiparra/obsidian-borealis) | `borealis` |  |
| [Bossidian](https://github.com/BossElijah/bossidian) | `bossidian` | Modern dark writing experience! |
| [Brainhack](https://github.com/Spekulucius/obsidian-brainhack) | `brainhack` |  |
| [Brutalism](https://github.com/abrahambahez/Brutalism) | `brutalism` |  |
| [Brutalist](https://github.com/DuckTapeKiller/Brutalist) | `brutalist` |  |
| [bubble-space](https://github.com/Emrie-Candera/Bubble-Space-Theme) | `bubble-space` |  |
| [Buena Vista](https://github.com/oqipoDev/buena-vista-obsidian) | `buena-vista` |  |
| [Camena](https://github.com/splendidissimemendax/Camena) | `camena` |  |
| [Carbon](https://github.com/vhbelvadi/obsidian-carbon) | `carbon` |  |
| [Cardstock](https://github.com/cassidoo/cardstock) | `cardstock` |  |
| [carnelian](https://github.com/gracejoseph1236/obsidian-carnelian) | `carnelian` |  |
| [carpe-noctem](https://github.com/operator-axel/obsdian_theme--Carpe_Noctem) | `carpe-noctem` |  |
| [Catppuccin](https://github.com/catppuccin/obsidian) | `catppuccin` |  |
| [Celestial Night](https://github.com/Bluemoondragon07/Obsidian-Celestial-Night-Theme) | `celestial-night` |  |
| [charcoal](https://github.com/bcdavasconcelos/Obsidian-Charcoal) | `charcoal` |  |
| [chiaroscuroflow](https://github.com/Quinta0/chiaroscuroflow) | `chiaroscuroflow` |  |
| [Cobalt Peacock](https://github.com/dpavaoman/cobalt-peacock-obmd) | `cobalt-peacock` |  |
| [Coffee](https://github.com/regawaras/Coffee) | `coffee` | Coffee Obsidian theme bringing duality of coffee flavors vibes through its dark (Dark Coffee) and light (Light Coffee) modes. This theme is designed to provide an ergonomic, soothing, and warm feel to your eyes, creating a comfortable working environment. |
| [Colored Candy](https://github.com/Erallie/colored-candy) | `colored-candy` |  |
| [Comfort](https://github.com/Carrie999/comfort) | `comfort` |  |
| [Comfort Dark](https://github.com/Ooopz/obsidianmd-theme-comfort-dark) | `comfort-dark` |  |
| [comfort-color-dark](https://github.com/obsidian-ezs/obsidian-comfort-color-dark) | `comfort-color-dark` |  |
| [comfort-smooth](https://github.com/sparklau/comfort-smooth) | `comfort-smooth` |  |
| [Composer](https://github.com/vran-dev/obsidian-composer) | `composer` |  |
| [Consolas](https://github.com/pinei/obsidian-consolas-theme) | `consolas` |  |
| [Cosmical](https://github.com/M-Torrus/obsidian-cosmical-theme) | `cosmical` |  |
| [Covert](https://github.com/schrunchee/obsidian-covert-theme) | `covert` |  |
| [Creme brulee](https://github.com/anareaty/creme-brulee-obsidian-theme) | `creme-brulee` |  |
| [Cupertino](https://github.com/aaaaalexis/obsidian-cupertino) | `cupertino` |  |
| [Cyber Glow](https://github.com/ThePharaohArt/Obsidian-CyberGlow) | `cyber-glow` |  |
| [Cybertron](https://github.com/nickmilo/Cybertron) | `cybertron` |  |
| [Cybertron Shifted](https://github.com/JorgEdmundo/cybertron-shifted) | `cybertron-shifted` |  |
| [Dark Castle](https://github.com/scottgriv/Dark-Castle-Obsidian) | `dark-castle` |  |
| [Dark Clarity](https://github.com/chenbihao/obsidian-theme-dark-clarity) | `dark-clarity` |  |
| [Dark Graphite Pie](https://github.com/ryjjin/Obsidian-Dark-Graphite-Pie-theme) | `dark-graphite-pie` |  |
| [Dark Moss](https://github.com/sergey900553/obsidian_githublike_theme) | `dark-moss` |  |
| [dark-graphite](https://github.com/bcdavasconcelos/Obsidian-Graphite) | `dark-graphite` |  |
| [DarkEmber](https://github.com/miz-i/Obsidian-theme-DarkEmber) | `darkember` |  |
| [Darkyan](https://github.com/johackim/obsidian-darkyan) | `darkyan` |  |
| [dashboard](https://github.com/incantatem2/Obsidian-dashboard) | `dashboard` |  |
| [Dawn](https://github.com/ds-package/Dawn) | `dawn` |  |
| [Dayspring](https://github.com/erykwalder/dayspring-theme) | `dayspring` |  |
| [Dedication](https://github.com/modigaphemelo/Dedication-obsidian-theme) | `dedication` |  |
| [Dedication 2](https://github.com/modigaphemelo/Dedication-2-Obsidian-Theme) | `dedication-2` |  |
| [deep submerge](https://github.com/incantatem2/Obsidian-deep-submerge) | `deep-submerge` |  |
| [deeper work](https://github.com/lucas-fern/obsidian-deeper-work-theme) | `deeper-work` |  |
| [Dekurai](https://github.com/sergey900553/obsidian_dekurai_theme) | `dekurai` |  |
| [Desserts](https://github.com/incantatem2/Obsidian-desserts) | `desserts` |  |
| [discordian](https://github.com/radekkozak/discordian) | `discordian` |  |
| [Dracula Gemini](https://github.com/clbn/dracula-gemini) | `dracula-gemini` |  |
| [Dracula Official](https://github.com/dracula/obsidian) | `dracula-official` |  |
| [Dracula Plus](https://github.com/saket61195/Dracula_obsidian_theme) | `dracula-plus` |  |
| [dracula-for-obsidian](https://github.com/jarodise/Dracula-for-Obsidian.md) | `dracula-for-obsidian` |  |
| [dracula-lyt](https://github.com/xRyul/ObsidianMD_Dracula_x_LYT) | `dracula-lyt` |  |
| [dracula-slim](https://github.com/bLaCkwEw/Dracula-Slim) | `dracula-slim` |  |
| [Duality](https://github.com/CascadeThemes/Duality) | `duality` |  |
| [Dune](https://github.com/Jopp-gh/Obsidian-Dune84) | `dune` |  |
| [Dunite](https://github.com/Ch0live/dunite) | `dunite` |  |
| [Dynamic Color](https://github.com/rodydavis/obsidian-dynamic-color) | `dynamic-color` |  |
| [Ebullientworks](https://github.com/ebullient/obsidian-theme-ebullientworks) | `ebullientworks` |  |
| [Eldritch](https://github.com/eldritch-theme/obsidian) | `eldritch` |  |
| [Elegance Enhanced](https://github.com/Victologo/elegance-theme) | `elegance` |  |
| [emerald](https://github.com/gracejoseph1236/obsidian-emerald) | `emerald` |  |
| [Emerald Echo](https://github.com/MalcolmMielle/Emerald-Echo) | `emerald-echo` |  |
| [Encore](https://github.com/Carbonateb/obsidian-encore-theme) | `encore` |  |
| [Enhanced file explorer tree](https://github.com/LennZone/enhanced-file-explorer-tree) | `enhanced-file-explorer-tree` |  |
| [Ethereon](https://github.com/ethereontheme/obsidian) | `ethereon` |  |
| [evangelion](https://github.com/xero/evangelion.obsidian) | `evangelion` |  |
| [everblush](https://github.com/Everblush/Obsidian) | `everblush` |  |
| [everforest](https://github.com/0xGlitchbyte/obsidian_everforest) | `everforest` |  |
| [Everforest Enchanted](https://github.com/FireIsGood/obsidian-everforest-enchanted) | `everforest-enchanted` |  |
| [Everforest Spruce](https://github.com/vupdivup/obsidian-everforest-spruce) | `everforest-spruce` |  |
| [Evergreen-Shadow](https://github.com/Quinta0/Evergreen-Shadow) | `evergreen-shadow` |  |
| [EvilRed](https://github.com/tu2-atmanand/EvilRed-ObsidianTheme) | `evilred` |  |
| [Faded](https://github.com/JoshKasap/Obsidian-Faded-Theme) | `faded` |  |
| [Fancy-a-Story](https://github.com/ElsaTam/obsidian-fancy-a-story) | `fancy-a-story` |  |
| [FastPpuccin](https://github.com/LostViking09/obsidian-fastppuccin) | `fastppuccin` |  |
| [Feather](https://github.com/zfmohammed/obsidian-feather) | `feather` |  |
| [firefly](https://github.com/lazercaveman/obsidian-firefly-theme) | `firefly` |  |
| [Flatcap](https://github.com/cheycron/flatcap-obsidian) | `flatcap` |  |
| [flexcyon](https://github.com/bladeacer/flexcyon) | `flexcyon` |  |
| [Flexoki](https://github.com/kepano/flexoki-obsidian) | `flexoki` |  |
| [Flexoki Warm](https://github.com/ofalvai/flexoki-warm) | `flexoki-warm` |  |
| [Focus](https://github.com/mProjectsCode/obsidian-focus-theme) | `focus` |  |
| [Frost](https://github.com/drkpxl/Frost) | `frost` |  |
| [Fusion](https://github.com/zamsyt/obsidian-fusion) | `fusion` |  |
| [Future](https://github.com/Bluemoondragon07/obsidian-future) | `future` |  |
| [Garden Gnome (Adwaita, GTK)](https://github.com/oqipoDev/garden-gnome-obsidian) | `garden-gnome-adwaita-gtk` |  |
| [gastown](https://github.com/dogwaddle/obsidian-gastown-theme.md) | `gastown` |  |
| [gdct](https://github.com/bcdavasconcelos/Obsidian-GDCT) | `gdct` |  |
| [gdct-dark](https://github.com/bcdavasconcelos/Obsidian-GDCT_Dark) | `gdct-dark` |  |
| [GitHub Theme](https://github.com/krios2146/obsidian-theme-github) | `github-theme` |  |
| [GitHubDHC](https://github.com/ScottKirvan/GitHubDHC) | `githubdhc` |  |
| [gitsidian](https://github.com/ismailgunacar/gitsidian) | `gitsidian` |  |
| [Glass Robo](https://github.com/lorens-osman-dev/Glass-Robo) | `glass-robo` |  |
| [golden-topaz](https://github.com/shaggyfeng/obsidian-Golden-Topaz-theme) | `golden-topaz` |  |
| [Green Nightmare](https://github.com/prradox/green-nightmare) | `green-nightmare` |  |
| [Gummy-Revived](https://github.com/WinnerWind/gummy-revived) | `gummy-revived` |  |
| [Hackthebox](https://github.com/golam71/obsidian-hackthebox) | `hackthebox` |  |
| [halcyon](https://github.com/dbarenholz/halcyon-obsidian) | `halcyon` |  |
| [Handwriting (Kalam)](https://github.com/kmranrg/obsidian-handwriting-theme) | `handwriting-kalam` | A clean and friendly handwriting-style theme using Kalam font, with colored headings and academic-friendly formatting. |
| [harmonic](https://github.com/Thiews/Obsidian-Harmonic) | `harmonic` |  |
| [Heboric](https://github.com/nhrrs/heboric-obsidian) | `heboric` |  |
| [Hidden Grotto](https://github.com/HotAndCold245/Hidden-Grotto) | `hidden-grotto` |  |
| [higlighter](https://github.com/lukauskas/obsidian-highlighter-theme) | `higlighter` |  |
| [hipstersmoothie](https://github.com/hipstersmoothie/hipstersmoothie-obsidian-theme) | `hipstersmoothie` |  |
| [Hojicha](https://github.com/pr0methevs/Hojicha) | `hojicha` |  |
| [HoverPopup](https://github.com/COGQOD/hoverpopup-obsidian-theme) | `hoverpopup` |  |
| [hulk](https://github.com/pgalliford/Obsidian-theme-Incredible-Hulk) | `hulk` |  |
| [Hydra Pressure](https://github.com/monoooki/obsidian-hydra-pressure-theme) | `hydra-pressure` |  |
| [iA Writer](https://github.com/mrowa44/obsidian-ia-writer) | `ia-writer` |  |
| [iB Writer](https://github.com/whereiswhere/iB-Writer) | `ib-writer` |  |
| [iceberg](https://github.com/izumin5210/obsidian-iceberg) | `iceberg` |  |
| [Improved Potato](https://github.com/DMeurer/improved-potato) | `improved-potato` |  |
| [Ink](https://github.com/harmtemolder/obsidian-ink) | `ink` |  |
| [ion](https://github.com/zamsyt/obsidian-ion) | `ion` |  |
| [Iridium](https://github.com/kyffa/Iridium) | `iridium` |  |
| [ITS Theme](https://github.com/SlRvb/Obsidian--ITS-Theme) | `its-theme` |  |
| [Jotter](https://github.com/lnbgc/obsidian-jotter) | `jotter` |  |
| [Kakano](https://github.com/isaacfreeman/kakano-obsidian-theme) | `kakano` |  |
| [Kanagawa](https://github.com/sspaeti/obsidian_kanagawa) | `kanagawa` |  |
| [Kanagawa Paper](https://github.com/sspaeti/obsidian_kanagawa_paper) | `kanagawa-paper` |  |
| [Kiwi Mono](https://github.com/c-sooyoung/kiwi-mono-obsidian-theme) | `kiwi-mono` |  |
| [Kurokula](https://github.com/Indyandie/kurokula-obsidian-theme) | `kurokula` |  |
| [Lagom](https://github.com/LeslyeCream/Lagom-Obsidian-Theme) | `lagom` |  |
| [LaTeX](https://github.com/benf2004/Obsidian-LaTeX-Theme) | `latex` |  |
| [Lavender-Mist](https://github.com/Quinta0/Lavender-Mist) | `lavender-mist` |  |
| [Lemons Theme](https://github.com/mProjectsCode/obsidian-lemons-theme) | `lemons-theme` |  |
| [LessWrong](https://github.com/outsidetext/lesswrong-obsidian) | `lesswrong` |  |
| [Light & Bright](https://github.com/Bluemoondragon07/obsidian-light-and-bright-theme) | `light-bright` |  |
| [Listive](https://github.com/efemkay/obsidian-listive-theme) | `listive` |  |
| [lizardmen-zettelkasten](https://github.com/dogwaddle/lizardmen-zettelkasten) | `lizardmen-zettelkasten` |  |
| [Lorens](https://github.com/lorens-osman-dev/Lorens-Obsidian-Theme) | `lorens` |  |
| [Lumines](https://github.com/danielkhmara/obsidian-lumines) | `lumines` |  |
| [LYT Mode](https://github.com/nickmilo/LYT-Mode) | `lyt-mode` |  |
| [Mado 11](https://github.com/hydescarf/Obsidian-Theme-Mado-11) | `mado-11` |  |
| [Mado Miniflow](https://github.com/hydescarf/Obsidian-Theme-Mado-Miniflow) | `mado-miniflow` |  |
| [mammoth](https://github.com/Wittionary/mammoth-obsidian-theme) | `mammoth` |  |
| [Maple](https://github.com/subframe7536/obsidian-theme-maple) | `maple` |  |
| [Marathon](https://github.com/Spekulucius/obsidian-marathon) | `marathon` |  |
| [Material 3](https://github.com/HarmfulBreeze/obsidian-material-3-theme) | `material-3` |  |
| [Material Flat](https://github.com/threethan/obsidian-material-flat-theme) | `material-flat` |  |
| [Material Gruvbox](https://github.com/AllJavi/material_gruvbox_obsidian) | `material-gruvbox` |  |
| [Material Ocean](https://github.com/dragonwocky/obsidian-material-ocean) | `material-ocean` |  |
| [Matrix](https://github.com/dubefab/Matrix) | `matrix` |  |
| [Meridian](https://github.com/mvahaste/meridian) | `meridian` |  |
| [Micro Mike](https://github.com/ThisTheThe/MicroMike) | `micro-mike` |  |
| [Midnight-Fjord](https://github.com/Quinta0/Midnight-Fjord) | `midnight-fjord` |  |
| [Minimal](https://github.com/kepano/obsidian-minimal) | `minimal` |  |
| [Minimal Dracula](https://github.com/druxorey/minimal-dracula-for-obsidian) | `minimal-dracula` |  |
| [Minimal Edge](https://github.com/hariiy-sys/Obsidian-Minimal-Edge) | `minimal-edge` |  |
| [Minimal Red](https://github.com/AfonsoMiranda02/MinimalRed-Obsidian-Theme) | `minimal-red` |  |
| [Minimal-Dark-Coder](https://github.com/Krishna-Sen-Programming-World/Minimal-Dark-Coder) | `minimal-dark-coder` | Provies Minimal Dark Coder like theme designed specifically for coders. Perfect for those who want a sleek, coder-friendly interface for their notes and projects. |
| [Minimalist Studio](https://github.com/david-troyer/obsidian-theme-minimalist-studio) | `minimalist-studio` |  |
| [Minimalists Paradise](https://github.com/bellebasso/Minimalists-Paradise) | `minimalists-paradise` |  |
| [Mint-Breeze](https://github.com/Quinta0/Mint-Breeze) | `mint-breeze` |  |
| [MistyMauve](https://github.com/RaveSplash/obsidian-misty-mauve) | `mistymauve` |  |
| [Modern GenZ Vibedose](https://github.com/omkar-4/Modern-GenZ-Vibedose) | `modern-genz-vibedose` |  |
| [modern-dark](https://github.com/roberts-code/obsidian-theme-modern-dark) | `modern-dark` |  |
| [mono black (monochrome, charcoal)](https://github.com/ZeChArtiahSaher/obsidian-mono-black) | `mono-black-monochrome-charcoal` |  |
| [Mono High Contrast](https://github.com/manuelcoca/obsidian-mono-high-contrast-theme) | `mono-high-contrast` |  |
| [monochroYOU](https://github.com/GuiMar10/monochroYou) | `monochroyou` |  |
| [Monokai](https://github.com/bitSchleuder/obsidian-monokai-theme) | `monokai` |  |
| [Monokai Ristretto](https://github.com/vinitkumar/monokai-ristretto-obsidian) | `monokai-ristretto` |  |
| [moonlight](https://github.com/kartik-karz/moonlight-obsidian) | `moonlight` |  |
| [Mulled Wine](https://github.com/incantatem2/Obsidian-mulled-wine) | `mulled-wine` |  |
| [Museifu Basic](https://github.com/account-not-relevant/museifu-basic-theme) | `museifu-basic` |  |
| [Mushin](https://github.com/Vlad3Design/Mushin) | `mushin` | A zen-inspired Obsidian theme embodying the Japanese concept of mushin - a state of no-mind, clarity, and effortless flow. Designed for deep focus and mental tranquility. |
| [Muted-Blue](https://github.com/HasanTheSyrian/Muted-Blue-Obsidian) | `muted-blue` |  |
| [Myst](https://github.com/mulder3062/Myst) | `myst` |  |
| [Neo](https://github.com/x0aa7i/obsidian-neo) | `neo` |  |
| [Neo Sploosh](https://github.com/monoooki/obsidian-neo-sploosh-theme) | `neo-sploosh` |  |
| [Neon Synthwave](https://github.com/grjsmith/Neon-Synthwave) | `neon-synthwave` |  |
| [Neovim](https://github.com/slavafyi/obsidian-neovim) | `neovim` |  |
| [NeuBorder](https://github.com/sq1000000/NeuBorder) | `neuborder` |  |
| [Neumorphism](https://github.com/LennZone/Neumorphism) | `neumorphism` |  |
| [Neutral Academia](https://github.com/incantatem2/Obsidian-neutral-academia) | `neutral-academia` |  |
| [NichNeumor](https://github.com/Nichtigott/NichNeumor) | `nichneumor` |  |
| [Nier](https://github.com/exloseur3d/nier-theme) | `nier` |  |
| [Night Owl](https://github.com/AstroAir/obsidian-night-owl) | `night-owl` |  |
| [Nightfox](https://github.com/markmacode/obsidian-nightfox) | `nightfox` |  |
| [Nightingale](https://github.com/frank0713/nightingale-obsidian) | `nightingale` |  |
| [Nightly Wolf](https://github.com/codejota/NightlyWolf_ObsidianTheme) | `nightly-wolf` |  |
| [nobb](https://github.com/buluw/nobb-obsidian) | `nobb` |  |
| [Noctilux](https://github.com/RastGame/obsidian-Noctilux) | `noctilux` |  |
| [Noctis](https://github.com/konnta0/obsidian-noctis-theme) | `noctis` | A theme for Obsidian based on Noctis' VS Code theme. |
| [Noctis Viola](https://github.com/konnta0/obsidian-noctis-viola-theme) | `noctis-viola` | A theme for Obsidian based on Noctis Viola VS Code theme. |
| [Nord](https://github.com/Lucas-Haux/Nord) | `nord` |  |
| [Nordic](https://github.com/natowb/obsidian-nordic) | `nordic` |  |
| [Northern-Sky](https://github.com/Quinta0/Northern-Sky) | `northern-sky` |  |
| [Nostromo](https://github.com/gvorbeck/Nostromo) | `nostromo` | An 80's retro-futuristic theme with comfortable, muted colors. Perfect for space-age note-taking without the eye strain. |
| [Nota Limonada Light](https://github.com/crishood/nota-limonada-light) | `nota-limonada-light` |  |
| [notation](https://github.com/deathau/Notation-for-Obsidian) | `notation` |  |
| [Notation 2](https://github.com/Bluemoondragon07/obsidian-notation-2) | `notation-2` |  |
| [NotSwift](https://github.com/davidjroos/obsidian-notswift) | `notswift` |  |
| [Novadust](https://github.com/mmartamg/novadust-obsidian) | `novadust` |  |
| [obsdn-dark-rmx](https://github.com/cannibalox/Obsdn-dark-rmx) | `obsdn-dark-rmx` |  |
| [Obsidian gruvbox](https://github.com/insanum/obsidian_gruvbox) | `obsidian-gruvbox` |  |
| [Obsidian Nord](https://github.com/insanum/obsidian_nord) | `obsidian-nord` |  |
| [obsidian-boom](https://github.com/sainadhx/obsidian-boom) | `obsidian-boom` |  |
| [obsidian-ia](https://github.com/rcvd/obsidian_ia) | `obsidian-ia` |  |
| [obsidian-windows-98-edition](https://github.com/SMUsamaShah/Obsidian-Win98-Edition) | `obsidian-windows-98-edition` |  |
| [obsidianite](https://github.com/bennyxguo/Obsidian-Obsidianite) | `obsidianite` |  |
| [Obsidianotion](https://github.com/diegoeis/obsidianotion) | `obsidianotion` |  |
| [obuntu](https://github.com/dmytrodubinin/Obuntu-theme-for-Obsidian) | `obuntu` |  |
| [OISTNB](https://github.com/omsandippatil/OISTNB) | `oistnb` |  |
| [Old World](https://github.com/double-tilde/old-world-obsidian) | `old-world` |  |
| [Oldsidian Purple](https://github.com/ltctceplrm/oldsidian-purple) | `oldsidian-purple` |  |
| [OLED.Black](https://github.com/Inc44/OLED.Black) | `oled-black` |  |
| [Olivier’s Theme](https://github.com/OlivierPS/Olivier-s-Theme) | `olivier-s-theme` |  |
| [Omega](https://github.com/OmegaCentauri68/Omega-Theme-for-Obsidian) | `omega` |  |
| [OneNice](https://github.com/Sunhaloo/OneNice) | `onenice` |  |
| [ono-sendai](https://github.com/cannibalox/ono-sendai_obsdn) | `ono-sendai` |  |
| [Orange](https://github.com/afrangi/Obsidian-Theme-Orange) | `orange` |  |
| [Oreo](https://github.com/carols12352/Oreo-theme) | `oreo` |  |
| [Origami](https://github.com/7368697661/Origami) | `origami` |  |
| [Origin](https://github.com/Bluemoondragon07/Obsidian-Origin) | `origin` |  |
| [Osaka Jade](https://github.com/sspaeti/obsidian_osaka_jade) | `osaka-jade` |  |
| [Oscura](https://github.com/vinitkumar/oscura-obsidian) | `oscura` |  |
| [Oxygen](https://github.com/davidvkimball/obsidian-oxygen) | `oxygen` |  |
| [Pale - 淡](https://github.com/hariiy-sys/obsidian-Pale) | `pale` |  |
| [panic-mode](https://github.com/bcdavasconcelos/Obsidian-Panic_Mode) | `panic-mode` |  |
| [Penumbra](https://github.com/jbisits/penumbra-obsidian-theme) | `penumbra` |  |
| [Perso](https://github.com/behrouze/obsidian-theme) | `perso` |  |
| [Phoenix](https://github.com/RyzenFromFire/obsidian-phoenix) | `phoenix` |  |
| [pine-forest-berry](https://github.com/Nilahn/pine_forest_berry) | `pine-forest-berry` |  |
| [pink-topaz](https://github.com/shaggyfeng/obsidian-Pink-topaz-theme) | `pink-topaz` |  |
| [pisum](https://github.com/GuangluWu/obsidian-pisum) | `pisum` |  |
| [Planetary](https://github.com/ninetyfive666/Planetary) | `planetary` |  |
| [Planetz Roller](https://github.com/monoooki/obsidian-planetz-roller-theme) | `planetz-roller` |  |
| [Playground](https://github.com/benjaminezequiel/playground-theme) | `playground` |  |
| [PLN](https://github.com/PipeItToDevNull/PLN) | `pln` |  |
| [Poimandres](https://github.com/yoGhastly/poimandres-obsidian) | `poimandres` |  |
| [Poimandres Extended](https://github.com/bastiangx/poimandres.obsidian) | `poimandres-extended` |  |
| [Polka](https://github.com/callumhackett/obsidian_polka_theme) | `polka` |  |
| [Pomme Notes](https://github.com/MrParalloid/pomme-notes) | `pomme-notes` |  |
| [Powered by Lancer](https://github.com/SourTarte/Powered-By-Lancer) | `powered-by-lancer` |  |
| [Powered by Lancer - Retouched](https://github.com/Cloopy/Powered-by-Lancer---Retouched) | `powered-by-lancer-retouched` |  |
| [Primary](https://github.com/primary-theme/obsidian) | `primary` |  |
| [Prime](https://github.com/rivea0/obsidian-prime) | `prime` |  |
| [Prism](https://github.com/damiankorcz/Prism-Theme) | `prism` |  |
| [Proper Dark](https://github.com/lukasbach/obsidian-proper-dark) | `proper-dark` |  |
| [ProtocolBlue](https://github.com/PrettyBoyCosmo/ProtocolBlue) | `protocolblue` |  |
| [Prussian Blue](https://github.com/EddieTheEd/Prussian-Blue) | `prussian-blue` |  |
| [Publisher](https://github.com/aidanastridge/Publisher) | `publisher` |  |
| [Pure](https://github.com/lychileng/Obsidian-Theme-Pure) | `pure` |  |
| [Purple Owl](https://github.com/zacharyc/purple-owl-theme) | `purple-owl` |  |
| [purple-aurora](https://github.com/AndreasStandar/Obsidian-Theme---Purple-Aurora) | `purple-aurora` |  |
| [Pxld](https://github.com/Lina674/Pxld-Obsidian-Theme) | `pxld` | This theme is inspired by pixelated games. |
| [Qlean](https://github.com/froq0/Qlean) | `qlean` |  |
| [Quietus](https://github.com/yuanzhixiang/obsidian-theme-quietus) | `quietus` |  |
| [Quillcode](https://github.com/theaayushpatel/quillcode) | `quillcode` |  |
| [Radiance](https://github.com/JabariD/obsidian-radiance) | `radiance` |  |
| [Ravenloft](https://github.com/circkumflexx/obsidian-ravenloft-theme) | `ravenloft` | A parchment-warm gothic theme inspired by AD&D 2e Ravenloft. Dual light/dark palettes, full typographic hierarchy. |
| [Red Graphite](https://github.com/seanwcom/Red-Graphite-for-Obsidian) | `red-graphite` |  |
| [Red-Shadow](https://github.com/DKLiberty/Red-Shadow) | `red-shadow` |  |
| [RedShift - OLED Blue Light Filter](https://github.com/norderan/RedShift-obsidian-theme) | `redshift-oled-blue-light-filter` |  |
| [Refined Default](https://github.com/FaisalTamanoJr/Refined-Default) | `refined-default` |  |
| [Reshi](https://github.com/contrapasso3/Reshi) | `reshi` |  |
| [Retro Windows](https://github.com/codeisconfusing/retro-windows-obsidian) | `retro-windows` |  |
| [Retroma](https://github.com/emarpiee/Retroma) | `retroma` |  |
| [RetroNotes](https://github.com/sr-campelo/retronotes) | `retronotes` |  |
| [RetroOS 98](https://github.com/ThePharaohArt/Obsidian-RetroOS98) | `retroos-98` |  |
| [reverie](https://github.com/santiyounger/Reverie-Obsidian-Theme) | `reverie` |  |
| [Rezin](https://github.com/NicolasGHS/Rezin-theme) | `rezin` |  |
| [Ribbons](https://github.com/ddspog/obsidian-ribbons-theme) | `ribbons` |  |
| [Rift](https://github.com/NoahBoos/obsidian-rift) | `rift` |  |
| [rmaki](https://github.com/luke-rmaki/rmaki-obsidian) | `rmaki` |  |
| [Robsi](https://github.com/Riffaells/Robsi) | `robsi` | Modern Material Design 3 theme with purple accents and blur effects |
| [ros-pine-moon](https://github.com/mimishahzad/rose-pine-moon-obsidian) | `ros-pine-moon` |  |
| [Rose Pine](https://github.com/rose-pine/obsidian) | `rose-pine` |  |
| [Rose Red](https://github.com/tu2-atmanand/RoseRed-ObsidianTheme) | `rose-red` |  |
| [Rosé Pine](https://github.com/sspaeti/obsidian_rose_pine) | `ros-pine` |  |
| [Royal Velvet](https://github.com/caro401/royal-velvet) | `royal-velvet` |  |
| [ruby](https://github.com/gracejoseph1236/obsidian-ruby) | `ruby` |  |
| [Sad Machine Druid](https://github.com/Halftroll0/Sad-Machine-Druid) | `sad-machine-druid` |  |
| [Sakurajima](https://github.com/Daiki48/sakurajima.obsidian) | `sakurajima` |  |
| [SALEM](https://github.com/SalemElatar/salem-obsidian-theme) | `salem` |  |
| [sanctum](https://github.com/jdanielmourao/obsidian-sanctum) | `sanctum` |  |
| [Sanctum reborn](https://github.com/antoKeinanen/obsidian-sanctum-reborn) | `sanctum-reborn` |  |
| [Sandover](https://github.com/eliz-abeth/sandover) | `sandover` |  |
| [Sandstorm](https://github.com/jaysan0/obsidian-sandstorm) | `sandstorm` |  |
| [Sanguine](https://github.com/Satchelmouth/Obsidian-Theme-Sanguine) | `sanguine` |  |
| [Sea Glass](https://github.com/KStew1017/obsidian-sea-glass-theme) | `sea-glass` |  |
| [Seamless View](https://github.com/GustavoSZ124/Obsidian-Theme-Seamless-View) | `seamless-view` |  |
| [Sei](https://github.com/iwa/Sei) | `sei` |  |
| [Serenity](https://github.com/Bluemoondragon07/Obsidian-Serenity) | `serenity` |  |
| [Serif](https://github.com/GodlyMan-bit/Serif) | `serif` |  |
| [Serika](https://github.com/Warrobot10/Serika-for-obsidian) | `serika` |  |
| [Shade Sanctuary](https://github.com/Elevict/Shade-Sanctuary) | `shade-sanctuary` |  |
| [Shadeflow](https://github.com/artorias305/obsidian-shadeflow) | `shadeflow` |  |
| [Shiba Inu](https://github.com/faroukx/Obsidian-shiba-inu-theme) | `shiba-inu` |  |
| [Shimmering Focus](https://github.com/chrisgrieser/shimmering-focus) | `shimmering-focus` |  |
| [Simple](https://github.com/diegoeis/simple-obsidian) | `simple` |  |
| [Simplicity](https://github.com/Thiews/obsidian-simplicity) | `simplicity` |  |
| [Simply Colorful](https://github.com/LorenzoPegorari/SimplyColorful) | `simply-colorful` |  |
| [Sodalite](https://github.com/tomzorz/Sodalite) | `sodalite` |  |
| [Solarized](https://github.com/harmtemolder/obsidian-solarized) | `solarized` |  |
| [Soli Deo Gloria](https://github.com/GodlyMan-bit/SoliDeoGloria) | `soli-deo-gloria` |  |
| [solitude](https://github.com/KyleKlus/solitude-obsidian-theme) | `solitude` |  |
| [Soloing](https://github.com/isax785/obsidian-soloing) | `soloing` |  |
| [Soothe](https://github.com/AwesomeDog/obsidian-soothe) | `soothe` |  |
| [Space](https://github.com/bhappen/obsidian-space) | `space` |  |
| [Sparkling Day](https://github.com/isax785/obsidian-sparkling-day) | `sparkling-day` |  |
| [Sparkling Night](https://github.com/isax785/obsidian-sparkling-night) | `sparkling-night` |  |
| [Spectrum Blue](https://github.com/SandmansDreams/Spectrum-Blue) | `spectrum-blue` |  |
| [SpectrumPlus](https://github.com/anotherlusitano/SpectrumPlus) | `spectrumplus` |  |
| [Spring](https://github.com/MateusHenriquegringo/spring-theme-obsidian) | `spring` |  |
| [Spy Terminal](https://github.com/IchiroFukuda/spy-terminal-theme) | `spy-terminal` |  |
| [sQdthOne](https://github.com/KeithLerner/ObsidianMDsQdthOne) | `sqdthone` |  |
| [Strict](https://github.com/Nikolai2038/strict-obsidian-theme) | `strict` |  |
| [subtlegold](https://github.com/kartik-karz/subtlegold-obsidian) | `subtlegold` |  |
| [suddha](https://github.com/dxcore35/Suddha-theme) | `suddha` |  |
| [Sunbather](https://github.com/babidisrc/obsidian-sunbather) | `sunbather` |  |
| [synthwave](https://github.com/marcoluzi/obsidian-synthwave) | `synthwave` |  |
| [Synthwave '84](https://github.com/G2Jose/synthwave-84-obsidian-theme) | `synthwave-84` |  |
| [Tech001](https://github.com/volodinroman/obsidian-tech001-theme) | `tech001` |  |
| [Terminal](https://github.com/zcysxy/Obsidian-Terminal-Theme) | `terminal` |  |
| [Terminal2K](https://github.com/isax785/Terminal2K) | `terminal2k` |  |
| [TerraFlow](https://github.com/dubefab/obsidian-TerraFlow) | `terraflow` |  |
| [theme-that-shall-not-be-named](https://github.com/ChopTV/Obsidian-Theme-That-Shall-Not-Be-Named) | `theme-that-shall-not-be-named` |  |
| [Things](https://github.com/colineckert/obsidian-things) | `things` |  |
| [Things 3](https://github.com/MrParalloid/obsidian-things) | `things-3` |  |
| [Tiniri](https://github.com/vladstudio/tiniri-obsidian) | `tiniri` |  |
| [Tokyo Night](https://github.com/tcmmichaelb139/obsidian-tokyonight) | `tokyo-night` |  |
| [Tokyo Night Simple](https://github.com/danarnold/tokyonight-simple) | `tokyo-night-simple` |  |
| [Tokyo Night Storm](https://github.com/arozx/obsidian_tokyo-night-storm) | `tokyo-night-storm` |  |
| [Tom's Theme](https://github.com/tomkaygames/Tom-s-Theme) | `tom-s-theme` |  |
| [Tomorrow](https://github.com/deudz/obsidian-tomorrow-theme) | `tomorrow` |  |
| [tomorrow-night-bright](https://github.com/gbraad-obsidian/obsidian-tomorrow-night-bright-theme) | `tomorrow-night-bright` |  |
| [Trace Labs](https://github.com/humandecoded/Trace-Labs-Obsidian-Theme) | `trace-labs` | This is the GitHub theme with color modifications made for Trace Labs |
| [traffic-lights](https://github.com/elliotboyd/obsidian-traffic-lights) | `traffic-lights` |  |
| [Transient](https://github.com/GeorgeAzma/Transient) | `transient` |  |
| [Transparent](https://github.com/Oczko24/Obsidian-transparent) | `transparent` |  |
| [True Black](https://github.com/kraasch/true-black) | `true-black` |  |
| [Typewriter](https://github.com/crashmoney/obsidian-typewriter) | `typewriter` |  |
| [Typomagical](https://github.com/hungsu/typomagical-obsidian) | `typomagical` |  |
| [Typora-Vue](https://github.com/ZekunC/Obsidian-Typora-Vue-Theme) | `typora-vue` |  |
| [Tyrone Neon](https://github.com/tyronejosee/tyrone-neon) | `tyrone-neon` |  |
| [Ukiyo](https://github.com/technerium/obsidian-ukiyo) | `ukiyo` |  |
| [Ultra Lobster](https://github.com/7368697661/Ultra-Lobster) | `ultra-lobster` |  |
| [Underwater](https://github.com/Seniblue/Underwater) | `underwater` |  |
| [Universitario](https://github.com/wulflo/obsidian-3Sumaq) | `universitario` |  |
| [ursa](https://github.com/obsidian-ezs/obsidian-ursa) | `ursa` |  |
| [Vanilla AMOLED](https://github.com/SakuraIsayeki/vanilla-amoled-theme) | `vanilla-amoled` |  |
| [Vanilla AMOLED Color](https://github.com/Sskki-exe/vanilla-amoled-theme-color) | `vanilla-amoled-color` |  |
| [Vanilla Palettes](https://github.com/GnRlLeclerc/Vanilla-Theme-Palettes) | `vanilla-palettes` |  |
| [Vauxhall](https://github.com/CyanVoxel/vauxhall-obsidian) | `vauxhall` |  |
| [Velocity](https://github.com/Gonzalo-D-Sales/obsidian-velocity) | `velocity` |  |
| [Velvet-Moon](https://github.com/Quinta0/Velvet-Moon) | `velvet-moon` |  |
| [Vercel Obsidian](https://github.com/en3sis/vercel-obsidian) | `vercel-geist` | A clean, modern Obsidian theme inspired by Vercel's design system with dark and light modes |
| [Vesnea Vibe](https://github.com/seavalanche/vesnea-obsidian-theme) | `vesnea-vibe` |  |
| [Vesper](https://github.com/omarrashad/obsidian-vesper) | `vesper` |  |
| [Vibrant](https://github.com/JamesLemony/obsidian_vibrant) | `vibrant` |  |
| [Vicious](https://github.com/zaheralmajed/vicious-theme-obsidian) | `vicious` |  |
| [violet-evening](https://github.com/aitaDev/Violet-Evening-for-Obsidian) | `violet-evening` |  |
| [Virgo](https://github.com/loveminimal/obsidian-theme-virgo) | `virgo` |  |
| [viridian](https://github.com/mulfok/obsidian-viridian) | `viridian` |  |
| [Vortex](https://github.com/abhimangs/obsidian-vortex) | `vortex` |  |
| [W95](https://github.com/phchang/W95) | `w95` |  |
| [wasp](https://github.com/santiyounger/Wasp-Obsidian-Theme) | `wasp` |  |
| [Wikipedia](https://github.com/Bluemoondragon07/Wikipedia-Theme) | `wikipedia` |  |
| [Willemstad](https://github.com/tingmelvin/willemstad-x) | `willemstad` |  |
| [Winter Spices](https://github.com/incantatem2/Obsidian-winter-spices) | `winter-spices` |  |
| [wombat](https://github.com/hush-hush/obsidian_wombat) | `wombat` |  |
| [WY Console](https://github.com/Satchelmouth/Obsidian-Theme-WYConsole) | `wy-console` |  |
| [Wyrd](https://github.com/curio-heart/obsidian-wyrd) | `wyrd` |  |
| [Xscriptor Theme](https://github.com/xscriptordev/obsidian) | `xscriptor` | A refined literary-inspired theme for Obsidian, featuring EB Garamond typography and flexible customization for any workspace. |
| [yin-and-yang](https://github.com/chetachiezikeuzor/Yin-and-Yang-Theme) | `yin-and-yang` |  |
| [Yue](https://github.com/GixoXYZ/YueObsidian) | `yue` |  |
| [Zario](https://github.com/nazarioricardo/zario-obsidian) | `zario` |  |
| [Zen](https://github.com/laughmaker/Zen) | `zen` |  |
| [Zenburn](https://github.com/danyim/obsidian-zenburn) | `zenburn` |  |
