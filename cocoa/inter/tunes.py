# Taken from https://github.com/abarnert/itunesterms

version = 1.1
path = '/Applications/iTunes.app'

classes = \
[('print_settings', b'pset'),
 ('application', b'capp'),
 ('artwork', b'cArt'),
 ('audio_CD_playlist', b'cCDP'),
 ('audio_CD_track', b'cCDT'),
 ('browser_window', b'cBrW'),
 ('device_playlist', b'cDvP'),
 ('device_track', b'cDvT'),
 ('encoder', b'cEnc'),
 ('EQ_preset', b'cEQP'),
 ('EQ_window', b'cEQW'),
 ('file_track', b'cFlT'),
 ('folder_playlist', b'cFoP'),
 ('item', b'cobj'),
 ('library_playlist', b'cLiP'),
 ('playlist', b'cPly'),
 ('playlist_window', b'cPlW'),
 ('radio_tuner_playlist', b'cRTP'),
 ('shared_track', b'cShT'),
 ('source', b'cSrc'),
 ('track', b'cTrk'),
 ('URL_track', b'cURT'),
 ('user_playlist', b'cUsP'),
 ('visual', b'cVis'),
 ('window', b'cwin')]

enums = \
[('track_listing', b'kTrk'),
 ('album_listing', b'kAlb'),
 ('cd_insert', b'kCDi'),
 ('standard', b'lwst'),
 ('detailed', b'lwdt'),
 ('stopped', b'kPSS'),
 ('playing', b'kPSP'),
 ('paused', b'kPSp'),
 ('fast_forwarding', b'kPSF'),
 ('rewinding', b'kPSR'),
 ('off', b'kRpO'),
 ('one', b'kRp1'),
 ('all', b'kAll'),
 ('small', b'kVSS'),
 ('medium', b'kVSM'),
 ('large', b'kVSL'),
 ('library', b'kLib'),
 ('iPod', b'kPod'),
 ('audio_CD', b'kACD'),
 ('MP3_CD', b'kMCD'),
 ('device', b'kDev'),
 ('radio_tuner', b'kTun'),
 ('shared_library', b'kShd'),
 ('unknown', b'kUnk'),
 ('albums', b'kSrL'),
 ('artists', b'kSrR'),
 ('composers', b'kSrC'),
 ('displayed', b'kSrV'),
 ('songs', b'kSrS'),
 ('none', b'kNon'),
 ('Books', b'kSpA'),
 ('folder', b'kSpF'),
 ('Genius', b'kSpG'),
 ('iTunes_U', b'kSpU'),
 ('Library', b'kSpL'),
 ('Movies', b'kSpI'),
 ('Music', b'kSpZ'),
 ('Party_Shuffle', b'kSpS'),
 ('Podcasts', b'kSpP'),
 ('Purchased_Music', b'kSpM'),
 ('TV_Shows', b'kSpT'),
 ('movie', b'kVdM'),
 ('music_video', b'kVdV'),
 ('TV_show', b'kVdT'),
 ('user', b'kRtU'),
 ('computed', b'kRtC')]

properties = \
[('copies', b'lwcp'),
 ('collating', b'lwcl'),
 ('starting_page', b'lwfp'),
 ('ending_page', b'lwlp'),
 ('pages_across', b'lwla'),
 ('pages_down', b'lwld'),
 ('error_handling', b'lweh'),
 ('requested_print_time', b'lwqt'),
 ('printer_features', b'lwpf'),
 ('fax_number', b'faxn'),
 ('target_printer', b'trpr'),
 ('current_encoder', b'pEnc'),
 ('current_EQ_preset', b'pEQP'),
 ('current_playlist', b'pPla'),
 ('current_stream_title', b'pStT'),
 ('current_stream_URL', b'pStU'),
 ('current_track', b'pTrk'),
 ('current_visual', b'pVis'),
 ('EQ_enabled', b'pEQ '),
 ('fixed_indexing', b'pFix'),
 ('frontmost', b'pisf'),
 ('full_screen', b'pFSc'),
 ('name', b'pnam'),
 ('mute', b'pMut'),
 ('player_position', b'pPos'),
 ('player_state', b'pPlS'),
 ('selection', b'sele'),
 ('sound_volume', b'pVol'),
 ('version', b'vers'),
 ('visuals_enabled', b'pVsE'),
 ('visual_size', b'pVSz'),
 ('data', b'pPCT'),
 ('description', b'pDes'),
 ('downloaded', b'pDlA'),
 ('format', b'pFmt'),
 ('kind', b'pKnd'),
 ('raw_data', b'pRaw'),
 ('artist', b'pArt'),
 ('compilation', b'pAnt'),
 ('composer', b'pCmp'),
 ('disc_count', b'pDsC'),
 ('disc_number', b'pDsN'),
 ('genre', b'pGen'),
 ('year', b'pYr '),
 ('location', b'pLoc'),
 ('minimized', b'pMin'),
 ('view', b'pPly'),
 ('band_1', b'pEQ1'),
 ('band_2', b'pEQ2'),
 ('band_3', b'pEQ3'),
 ('band_4', b'pEQ4'),
 ('band_5', b'pEQ5'),
 ('band_6', b'pEQ6'),
 ('band_7', b'pEQ7'),
 ('band_8', b'pEQ8'),
 ('band_9', b'pEQ9'),
 ('band_10', b'pEQ0'),
 ('modifiable', b'pMod'),
 ('preamp', b'pEQA'),
 ('update_tracks', b'pUTC'),
 ('container', b'ctnr'),
 ('id', b'ID  '),
 ('index', b'pidx'),
 ('persistent_ID', b'pPIS'),
 ('duration', b'pDur'),
 ('parent', b'pPlP'),
 ('shuffle', b'pShf'),
 ('size', b'pSiz'),
 ('song_repeat', b'pRpt'),
 ('special_kind', b'pSpK'),
 ('time', b'pTim'),
 ('visible', b'pvis'),
 ('capacity', b'capa'),
 ('free_space', b'frsp'),
 ('album', b'pAlb'),
 ('album_artist', b'pAlA'),
 ('album_rating', b'pAlR'),
 ('album_rating_kind', b'pARk'),
 ('bit_rate', b'pBRt'),
 ('bookmark', b'pBkt'),
 ('bookmarkable', b'pBkm'),
 ('bpm', b'pBPM'),
 ('category', b'pCat'),
 ('comment', b'pCmt'),
 ('database_ID', b'pDID'),
 ('date_added', b'pAdd'),
 ('enabled', b'enbl'),
 ('episode_ID', b'pEpD'),
 ('episode_number', b'pEpN'),
 ('EQ', b'pEQp'),
 ('finish', b'pStp'),
 ('gapless', b'pGpl'),
 ('grouping', b'pGrp'),
 ('long_description', b'pLds'),
 ('lyrics', b'pLyr'),
 ('modification_date', b'asmo'),
 ('played_count', b'pPlC'),
 ('played_date', b'pPlD'),
 ('podcast', b'pTPc'),
 ('rating', b'pRte'),
 ('rating_kind', b'pRtk'),
 ('release_date', b'pRlD'),
 ('sample_rate', b'pSRt'),
 ('season_number', b'pSeN'),
 ('shufflable', b'pSfa'),
 ('skipped_count', b'pSkC'),
 ('skipped_date', b'pSkD'),
 ('show', b'pShw'),
 ('sort_album', b'pSAl'),
 ('sort_artist', b'pSAr'),
 ('sort_album_artist', b'pSAA'),
 ('sort_name', b'pSNm'),
 ('sort_composer', b'pSCm'),
 ('sort_show', b'pSSN'),
 ('start', b'pStr'),
 ('track_count', b'pTrC'),
 ('track_number', b'pTrN'),
 ('unplayed', b'pUnp'),
 ('video_kind', b'pVdK'),
 ('volume_adjustment', b'pAdj'),
 ('address', b'pURL'),
 ('shared', b'pShr'),
 ('smart', b'pSmt'),
 ('bounds', b'pbnd'),
 ('closeable', b'hclb'),
 ('collapseable', b'pWSh'),
 ('collapsed', b'wshd'),
 ('position', b'ppos'),
 ('resizable', b'prsz'),
 ('zoomable', b'iszm'),
 ('zoomed', b'pzum')]

elements = \
[('artworks', b'cArt'),
 ('audio_CD_playlists', b'cCDP'),
 ('audio_CD_tracks', b'cCDT'),
 ('browser_windows', b'cBrW'),
 ('device_playlists', b'cDvP'),
 ('device_tracks', b'cDvT'),
 ('encoders', b'cEnc'),
 ('EQ_presets', b'cEQP'),
 ('EQ_windows', b'cEQW'),
 ('file_tracks', b'cFlT'),
 ('folder_playlists', b'cFoP'),
 ('items', b'cobj'),
 ('library_playlists', b'cLiP'),
 ('playlists', b'cPly'),
 ('playlist_windows', b'cPlW'),
 ('radio_tuner_playlists', b'cRTP'),
 ('shared_tracks', b'cShT'),
 ('sources', b'cSrc'),
 ('tracks', b'cTrk'),
 ('URL_tracks', b'cURT'),
 ('user_playlists', b'cUsP'),
 ('visuals', b'cVis'),
 ('windows', b'cwin'),
 ('application', b'capp'),
 ('print_settings', b'pset')]

commands = \
[('set', b'coresetd', [('to', b'data')]),
 ('exists', b'coredoex', []),
 ('move', b'coremove', [('to', b'insh')]),
 ('subscribe', b'hookpSub', []),
 ('playpause', b'hookPlPs', []),
 ('download', b'hookDwnl', []),
 ('close', b'coreclos', []),
 ('open', b'aevtodoc', []),
 ('open_location', b'GURLGURL', []),
 ('quit', b'aevtquit', []),
 ('pause', b'hookPaus', []),
 ('make',
  'corecrel',
  [('new', b'kocl'), ('at', b'insh'), ('with_properties', b'prdt')]),
 ('duplicate', b'coreclon', [('to', b'insh')]),
 ('print_',
  'aevtpdoc',
  [('print_dialog', b'pdlg'),
   ('with_properties', b'prdt'),
   ('kind', b'pKnd'),
   ('theme', b'pThm')]),
 ('add', b'hookAdd ', [('to', b'insh')]),
 ('rewind', b'hookRwnd', []),
 ('play', b'hookPlay', [('once', b'POne')]),
 ('run', b'aevtoapp', []),
 ('resume', b'hookResu', []),
 ('updatePodcast', b'hookUpd1', []),
 ('next_track', b'hookNext', []),
 ('stop', b'hookStop', []),
 ('search', b'hookSrch', [('for_', b'pTrm'), ('only', b'pAre')]),
 ('updateAllPodcasts', b'hookUpdp', []),
 ('update', b'hookUpdt', []),
 ('previous_track', b'hookPrev', []),
 ('fast_forward', b'hookFast', []),
 ('count', b'corecnte', [('each', b'kocl')]),
 ('reveal', b'hookRevl', []),
 ('convert', b'hookConv', []),
 ('eject', b'hookEjct', []),
 ('back_track', b'hookBack', []),
 ('refresh', b'hookRfrs', []),
 ('delete', b'coredelo', [])]
